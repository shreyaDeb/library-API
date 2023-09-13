from django.contrib.auth.models import Permission

# managing books

can_add_book = Permission.objects.create(
    codename='can_add_book',
    name='Can add book',
)

can_edit_book = Permission.objects.create(
    codename='can_edit_book',
    name='Can edit book',
)

can_delete_book = Permission.objects.create(
    codename='can_delete_book',
    name='Can delete book',
)

# managing users

can_add_user = Permission.objects.create(
    codename='can_add_user',
    name='can add user',
)

can_edit_user = Permission.objects.create(
    codename='can_edit_user',
    name='Can edit user',
)

can_delete_user = Permission.objects.create(
    codename='can_delete_user',
    name='Can delete user',
)

# managing employees

can_add_employee = Permission.objects.create(
    codename='can_add_employee',
    name='can add employee',
)

can_edit_employee = Permission.objects.create(
    codename='can_edit_employee',
    name='can edit employee',
)

can_delete_employee = Permission.objects.create(
    codename='can_delete_employee',
    name='can delete employee',
)

# Assign permissions to roles
user_role = UserRole.objects.get(name='user')
employee_role = UserRole.objects.get(name='employee')
admin_employee_role = UserRole.objects.get(name='admin employee')

user_role.permissions.add(can_add_book)  # Users can add books
employee_role.permissions.add(can_add_book, can_edit_book, can_delete_book, can_add_user, can_edit_user, can_delete_user)  # Employees can add, edit, and delete books
admin_employee_role.permissions.add(can_add_book, can_edit_book, can_delete_book, can_add_employee, can_edit_employee, can_delete_employee, can_add_user, can_edit_user, can_delete_user)  # Admin employees have the same permissions as employees
