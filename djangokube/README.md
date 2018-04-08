# Books & Movies Wishlist

A simple Django app deployed with Kubernetes using Google Container Engine.

It displays a list of books and movies that users plan to read / watch. Once an item no longer belongs to the wishlist, it can be simply removed (an AJAX request is sent to the Django server in the background).


Future plans:

1. Add proper url redirects;
2. Use some public API for auto-suggesting books and movies (eg. if users don't remember full titles);
3. Manage secrets properly in Kubernetes;
4. Add persistent volumes in Kubernetes;
5. Write better media queries.
