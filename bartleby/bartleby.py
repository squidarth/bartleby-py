import sys
import redis

class Bartleby(object):
  def __init__(self, files, redis_host="localhost", redis_port=6379):
    self.redis = redis.StrictRedis(host=redis_host, port=redis_port) 
    sys.settrace(self.traceit)
    self.files = files
    self.local_variables = {}
    self.global_variables = {}

  def traceit(self, frame, event, arg):
    if event == "line":
      lineno = frame.f_lineno

      if "__file__" in frame.f_globals:
        filename = frame.f_globals["__file__"]

        if filename in self.files:
          report_list = [] 
          for key in frame.f_globals:
            # If it's the same, check the value 
            if key in self.global_variables:
              if frame.f_globals[key] != self.global_variables[key]:
                report_list.append("%s:%s, %s:%s" % (filename, lineno, key, frame.f_globals[key]))
            else:
              report_list.append("%s:%s, %s:%s" % (filename, lineno, key, frame.f_globals[key]))
            self.global_variables[key] = frame.f_globals[key]
          for key in frame.f_locals:
            # If it's the same, check the value 
            if key in self.global_variables:
              if frame.f_locals[key] != self.global_variables[key]:
                report_list.append("%s:%s, %s:%s" % (filename, lineno, key, frame.f_locals[key]))
            else:
              report_list.append("%s:%s, %s:%s" % (filename, lineno, key, frame.f_locals[key]))

            self.global_variables[key] = frame.f_locals[key]

          print("\n".join(report_list))
          print(len(report_list))
          self.redis.publish("bartleby"," \n ".join(report_list))

    return self.traceit
