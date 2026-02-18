# PasswordStrengthChecker
A simple python password strength checker

How to run:
To run this code import it into any python IDE (this program was developed in Spyder and that is recommended) and press run. Alternatively you can run it from the command line the same way you could any other python script.
This program has no other dependencies.

Limitations:
This tool is meant for educational purposes only and should not be used for actual security measures.

The strength of a password is determined by the first figure here: https://www.hivesystems.com/blog/are-your-passwords-in-the-green
where purple was treated as very weak, red as weak, orange as normal, yellow as strong, and green as very strong.

The strength calculations for a numbers only password is extrapolated beyond 18 characters, using the smallest values of the next tier up to determine minimum values needed.
Beyond 18 characters time was multipled by 10 to account for another factor of 10 digits to test for, this appears to follow an the established pattern from 13-17 characters.
As such numeric passwords beyond 18 characters may not accurately represent the real strength of that password.

Ethical Considerations/Responsible Use:
This tool is meant for educational purposes only and should not be used for actual security measures.
This password checker is based on data that has been gathered and makes many assumptions, this password strength checker should not be used in production settings.
Please remember to change your passwords regularly and to not share passwords between sites, shared and leaked passwords reduce the strength of passwords to almost nothing.
This password checker assumes modern hashing best practices, please remember to use them.
In theory this program could be modified to log passwords whose strength people want to check, I would ask that you do not do this.
