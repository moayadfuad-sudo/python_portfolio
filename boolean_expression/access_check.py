#access_check.py
MAX_FAILED=5
role=input("Role:")
mfa_answer=input("MFA passed? (yes/no):")
failed=int(input("failed attmpts:"))

mfa_ok= mfa_answer == "yes"
is_privileged= role == "admin" or role == "root"
can_log_in= mfa_ok and is_privileged and failed < MAX_FAILED

print(f"MFA passed: {mfa_ok}")
print(f"privileged role: {is_privileged}")
print(f"can log in: {can_log_in}")