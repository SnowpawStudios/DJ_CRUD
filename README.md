# DJ_CRUD

This is a simple django app that serves as a template for using function based views and modelforms to perform crud operations.

Main features:
- Function based views to perform create, read, update, and delete operations
- Model forms to quickly create forms directly linked to a model
- Register a model in admin so it can be viewed in django admin
- Url mapping to a specific app
- Shows how to setup a template folder at the project level and inherit from a base template
- Shows how to setup global static files (css, js, images) from a project level folder and how to link to this in the base template
- Separate User app, with 1-to-1 relationship between Django's built in User model and a custom Profile model.
- Signals to let the User and Profile Models interact with each other.
- Basic authentication, login, signup, using function based views.

Other:
- Created static paths in settings for user uploaded images
- installed pillow to help deal with images
- installed whitenoise and created a path to a staticfiles and static_root to prepare for serving static files in deployment

TODO:
Redo basic styling using bulma