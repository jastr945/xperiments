# Elasticsearch App

A renponsive Django web app providing ***a full-text search engine*** for finding articles related to Cannon Beach, Oregon. The search tab has an autocomplete functionality, which allows users to pick a title from the drop-down list after typing just a few letters. Queries can include words and phrases. Matching search terms are highlighted for better usability.

### Specific functionality
- Elasticsearch library with elasticsearch-dsl and django-elasticsearch-dsl clients for searching through the database
- Elasticsearch installed with Docker
- JqueryUI Autocomplete plugin using data from the Django view via an AJAX call
- Customized rich-text editor built into the admin interface
- Matching search terms are highlighted with the custom template tag
- Responsive Bootstrap front-end
