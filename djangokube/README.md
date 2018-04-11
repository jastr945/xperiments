# Books & Movies Wishlist

A simple Django app deployed with Kubernetes using Google Container Engine.

This app helps you to keep track of books and movies that you plan to check out. It displays a list of books and movies that people recommended you to read / watch. Once an item no longer belongs to the wishlist, it can be simply removed (an AJAX request is sent to the Django server in the background).

Login with Google is provided by Auth0[https://auth0.com/].


Future plans:

1. Use some public API for auto-suggesting books and movies (eg. if users don't remember full titles);
2. Manage secrets properly in Kubernetes;
3. Add persistent volumes in Kubernetes;
