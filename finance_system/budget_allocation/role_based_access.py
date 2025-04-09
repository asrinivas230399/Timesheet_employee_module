# role_based_access.py

def is_authorized(role):
    # Mock authorization check
    authorized_roles = ['finance_team', 'admin']
    return role in authorized_roles
