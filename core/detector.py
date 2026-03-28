# Detection logic

def analyze_log(log):

    if "LOGIN FAILED" in log:
        return "Failed login detected"

    if "LOGIN SUCCESS - admin" in log:
        return "Admin login detected"

    if "confidential" in log:
        return "Sensitive file access detected"

    return None
