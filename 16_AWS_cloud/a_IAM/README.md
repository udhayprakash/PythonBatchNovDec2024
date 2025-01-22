IAM 

    Users   (Human beings)
    Roles   (Resources/Machines)
    Groups   (group the permissions, as needed)
    Permissions  (each specific )


          +--------------------+
          |    IAM Policies    |
          +--------------------+
                  ▲
                  |
                  |
+-----------------+------------------+
|                                    |
|                                    |
▼                                    ▼
+--------------------+      +--------------------+
|     IAM Users      |      |     IAM Roles      |
+--------------------+      +--------------------+
           ▲                        ▲
           |                        |
           |                        |
           ▼                        ▼
    +--------------------+   +--------------------+
    |   IAM User Groups  |   |   Trusted Entities |
    +--------------------+   +--------------------+


Explanation of Relationships

IAM Policies:
    Define permissions (allow/deny actions on resources).
    Can be attached to users, roles, or groups.

IAM Users:
    Represent individual people or applications.
    Can have policies directly attached or inherit them via groups.

IAM User Groups:
    Aggregate multiple users for easier permission management.
    Policies attached to a group apply to all its members.

IAM Roles:
    Provide temporary credentials for access.
    Assumable by trusted entities (e.g., users, services, or external identities).
    Have policies attached to define permissions.

Trusted Entities:
    Specify who can assume a role (e.g., AWS services, IAM users, or external identity providers).



Steps 
=====
1) created the IAM Group : PythonUserGroup
2) attached the policies: s3FullAccess, LambdaFullAccess
3) Created IAM User: PythonUser
4) Attchad the User group : Pytjon UserGroup to it 