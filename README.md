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
### 3. ABOUT APP
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


### -----------------
### 4. CONTACT APP
### -----------------


#### 4.1 Create contact app


#### 4.2 Register the app to project

        modified:   README.md
        modified:   apps/contact/apps.py
        modified:   config/settings.py


#### 4.3 Create contact_page and link to menu

        modified:   README.md
        new file:   apps/contact/urls.py
        modified:   apps/contact/views.py
        modified:   config/urls.py
        modified:   templates/about/about_page.html
        new file:   templates/contact/contact_page.html
        modified:   templates/shared/header_desktop_menu.html
        modified:   templates/shared/header_mobile_menu.html
        modified:   templates/shared/header_topbar.html
        new file:   templates/shared/sidebar_popular_posts.html


### -------------
### 5. NEWS APP
### -------------


#### 5.1 Create a new app 'apps/news'


#### 5.2 Register news app to project

        modified:   README.md
        modified:   apps/news/apps.py
        modified:   config/settings.py



### --------------
### 6. ADMIN APP
### --------------


#### 6.1 Create a new app 'apps/admin'


#### 6.2 Register news app to project

        modified:   README.md
        modified:   apps/admin/apps.py
        modified:   config/settings.py


#### 6.3 Re-naming the app from admin to dashboard, create admin home_page_admin (VT Urls) and menu

        modified:   README.md
        deleted:    apps/admin/views.py
        renamed:    apps/admin/admin.py -> apps/dashboard/admin.py
        renamed:    apps/admin/apps.py -> apps/dashboard/apps.py
        renamed:    apps/admin/models.py -> apps/dashboard/models.py
        renamed:    apps/admin/tests.py -> apps/dashboard/tests.py
        new file:   apps/dashboard/urls.py
        new file:   apps/dashboard/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   templates/dashboard/home_page_dashboard.html
        modified:   templates/shared/header_topbar.html


#### 6.4 Add html template to home_page_dashboard, static files and load static

        modified:   README.md
        ...
        new file:   static_in_env/dashboard/less/themes/night.less
        new file:   static_in_env/dashboard/less/themes/spring.less
        new file:   static_in_env/dashboard/less/themes/waterlily.less
        new file:   static_in_env/dashboard/less/variables.less
        modified:   templates/dashboard/home_page_dashboard.html


#### 6.5 Customize Admin Panel Part 1

        modified:   README.md
        modified:   templates/dashboard/home_page_dashboard.html


#### 6.6 Customize Admin Panel Part 2

        modified:   README.md
        modified:   templates/dashboard/home_page_dashboard.html


#### 6.7 Customize Admin Panel Part 3

        modified:   README.md
        modified:   templates/dashboard/home_page_dashboard.html


#### 6.8 Customize Admin Panel Part 4 - Sagmenting home_page_dashboard

        modified:   README.md
        modified:   templates/dashboard/home_page_dashboard.html
        new file:   templates/dashboard/shared/dashboard_content.html
        new file:   templates/dashboard/shared/dashboard_footer.html
        new file:   templates/dashboard/shared/dashboard_header.html
        new file:   templates/dashboard/shared/scripts.html
        new file:   templates/dashboard/shared/sidebar.html
        new file:   templates/dashboard/shared/user_settings.html






























































































































































