# customise-user-model
AbstractUser vs AbstractBaseUser
The default user model in Django uses a username to uniquely identify a user during authentication. If you'd rather use an email address, you'll need to create a custom user model by either subclassing AbstractUser or AbstractBaseUser.

Options:

AbstractUser: Use this option if you are happy with the existing fields on the user model and just want to remove the username field.
AbstractBaseUser: Use this option if you want to start from scratch by creating your own, completely new user model.



The steps are the same for each:

Create a custom user model and Manager
Update settings.py
Customize the UserCreationForm and UserChangeForm forms
Update the admin
It's highly recommended to set up a custom user model when starting a new Django project. Without it, you will need to create another model (like UserProfile) and link it to the Django user model with a OneToOneField if you want to add new fields to the user model.
