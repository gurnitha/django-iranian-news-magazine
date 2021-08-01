## BUILDING NEWS MAGAZINE APPLICATION USING DJANGO V.3.2


### -----------------
### 1. BASICS SETUP
### -----------------


#### 1.1 Creata venv and install django v3.2

#### 1.2 Create django project and app

#### 1.3 Register main app to project

        modified:   README.md
        modified:   apps/main/apps.py
        modified:   config/settings.py


### --------------
### 2. HOME PAGE
### --------------


#### 2.1 Create hello world using Views, Templates, and Urls

        modified:   README.md
        new file:   apps/main/urls.py
        modified:   apps/main/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   db.sqlite3
        new file:   templates/main/home_page.html


#### 2.2 Creating path for static and media files

        modified:   README.md
        modified:   config/settings.py
        modified:   config/urls.py


#### 2.3 Adding static files and html template for the home page

        modified:   README.md
        ...
        new file:   static_in_env/vendor/bootstrap/js/tooltip.js
        new file:   static_in_env/vendor/css-hamburgers/hamburgers.css
        new file:   static_in_env/vendor/css-hamburgers/hamburgers.min.css
        new file:   static_in_env/vendor/jquery/jquery-3.2.1.min.js
        modified:   templates/main/home_page.html


#### 2.4 Loading static files

        modified:   README.md
        modified:   templates/main/home_page.html


#### 2.5 Sagmenting the home page

        modified:   README.md
        modified:   templates/main/home_page.html
        new file:   templates/shared/footer_categories.html
        new file:   templates/shared/footer_copyright.html
        new file:   templates/shared/footer_info.html
        new file:   templates/shared/footer_popular_posts.html
        new file:   templates/shared/footer_scripts.html
        new file:   templates/shared/head.html
        new file:   templates/shared/header_desktop_menu.html
        new file:   templates/shared/header_logo_desktop.html
        new file:   templates/shared/header_logo_mobile.html
        new file:   templates/shared/header_mobile_menu.html
        new file:   templates/shared/header_topbar.html


#### 2.6 Base template

        modified:   README.md
        new file:   templates/base.html
        modified:   templates/main/home_page.html


#### 2.7 Sagmenting the main content of the home page

        modified:   templates/main/home_page.html
        new file:   templates/main/inc/banner.html
        new file:   templates/main/inc/latest.html
        new file:   templates/main/inc/post_aside.html
        new file:   templates/main/inc/post_business.html
        new file:   templates/main/inc/post_entertaiment.html
        new file:   templates/main/inc/post_travel.html


### ---------------
### 3. ABOUT PAGE
### ---------------


#### 3.1 Create about app 'apps/about'


#### 3.2 Register the about app to project

        modified:   README.md
        modified:   apps/about/apps.py
        modified:   config/settings.py


#### 3.3 Add About page (Views, Templates, Urls)

        modified:   README.md
        new file:   apps/about/urls.py
        modified:   apps/about/views.py
        modified:   config/urls.py
        new file:   templates/about/about_page.html
        deleted:    templates/about_page.html
        modified:   templates/shared/head.html


#### 3.4 Linking the pages

        modified:   templates/shared/header_desktop_menu.html
        modified:   templates/shared/header_logo_desktop.html
        modified:   templates/shared/header_logo_mobile.html
        modified:   templates/shared/header_mobile_menu.html
        modified:   templates/shared/header_topbar.html
































































































































































































