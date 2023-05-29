from django.urls import path
from admin_tabler import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),

    # Interface
    path('accordion/', views.accordion, name='accordion'),
    path('blank-page/', views.blank_page, name='blank_page'),
    path('badges/', views.badges, name='badges'),
    path('buttons/', views.buttons, name='buttons'),
    # Cards
    path('cards/sample-cards/', views.sample_cards, name='cards'),
    path('cards/card-actions/', views.card_actions, name='card_actions'),
    path('cards/cards-masonry/', views.cards_masonry, name='cards_masonry'),

    path('colors/', views.colors, name='colors'),
    path('data-grid/', views.data_grid, name='data_grid'),
    path('datatables/', views.datatables, name='datatables'),
    path('dropdowns/', views.dropdowns, name='dropdowns'),
    path('modals/', views.modals, name='modals'),
    path('maps/', views.maps, name='maps'),
    path('map-fullsize/', views.map_fullsize, name='map_fullsize'),
    path('vector-maps/', views.vector_maps, name='vector_maps'),
    path('navigation/', views.navigation, name='navigation'),
    path('charts/', views.charts, name='charts'),
    path('pagination/', views.pagination, name='pagination'),
    path('placeholder/', views.placeholder, name='placeholder'),
    path('steps/', views.steps, name='steps'),
    path('stars-rating/', views.stars_rating, name='stars_rating'),
    path('tabs/', views.tabs, name='tabs'),
    path('tables/', views.tables, name='tables'),
    path('carousel/', views.carousel, name='carousel'),
    path('lists/', views.lists, name='lists'),
    path('typography/', views.typography, name='typography'),
    path('offcanvas/', views.offcanvas, name='offcanvas'),
    path('markdown/', views.markdown, name='markdown'),
    path('dropzone/', views.dropzone, name='dropzone'),
    path('lightbox/', views.lightbox, name='lightbox'),
    path('tinymce/', views.tinymce, name='tinymce'),
    path('inline-player/', views.inline_player, name='inline_player'),

    # Authentication
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/login-illustration/', views.LoginViewIllustrator.as_view(), name='login_illustration'),
    path('accounts/login-cover/', views.LoginViewCover.as_view(), name='login_cover'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/login-link/', views.login_link, name='login_link'),
    path('accounts/register/', views.RegistrationView.as_view(), name='register'),
    path('terms-service/', views.terms_service, name='terms_service'),
    path('accounts/lock-screen/', views.lock_screen, name='lock_screen'),

    path('accounts/password-change/', views.UserPasswordChangeView.as_view(), name='change_password'),
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='pages/password-change-done.html'
    ), name="password_change_done" ),

    path('accounts/forgot-password/', views.PasswordReset.as_view(), name='forgot_password'),
    path('accounts/password-reset-confirm/<uidb64>/<token>/', 
        views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='pages/password-reset-done.html'
    ), name='password_reset_done'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='pages/password-reset-complete.html'
    ), name='password_reset_complete'),

    # Error
    path('error/404/', views.error_404, name='error_404'),
    path('error/500/', views.error_500, name='error_500'),
    path('error/maintenance/', views.maintenance, name='maintenance'),

    path('form-elements/', views.form_elements, name='form_elements'),

    # Extra
    path('empty-page/', views.empty_page, name='empty_page'),
    path('cookie-banner/', views.cookie_banner, name='cookie_banner'),
    path('activity/', views.activity, name='activity'),
    path('gallery/', views.gallery, name='gallery'),
    path('invoice/', views.invoice, name='invoice'),
    path('search-results/', views.search_results, name='search_results'),
    path('pricing-cards/', views.pricing_cards, name='pricing_cards'),
    path('pricing-table/', views.pricing_table, name='pricing_table'),
    path('faq/', views.faq, name='faq'),
    path('users/', views.users, name='users'),
    path('license/', views.license, name='license'),
    path('logs/', views.logs, name='logs'),
    path('music/', views.music, name='music'),
    path('photogrid/', views.photogrid, name='photogrid'),
    path('tasks/', views.tasks, name='tasks'),
    path('uptime/', views.uptime, name='uptime'),
    path('widgets/', views.widgets, name='widgets'),
    path('wizard/', views.wizard, name='wizard'),
    path('settings/', views.settings, name='settings'),
    path('settings-plan/', views.settings_plan, name='settings_plan'),
    path('trial-ended/', views.trial_ended, name='trial_ended'),
    path('job-listing/', views.job_listing, name='job_listing'),
    path('page-loader/', views.page_loader, name='page_loader'),

    # Layout
    path('layout/horizontal/', views.layout_horizontal, name='layout_horizontal'),
    path('layout/boxed/', views.layout_boxed, name='layout_boxed'),
    path('layout/vertical/', views.layout_vertical, name='layout_vertical'),
    path('layout/vertical-transparent/', views.layout_vertical_transparent, name='layout_vertical_transparent'),
    path('layout/vertical-right/', views.layout_vertical_right, name='layout_vertical_right'),
    path('layout/condensed/', views.layout_condensed, name='layout_condensed'),
    path('layout/combined/', views.layout_combined, name='layout_combined'),
    path('layout/navbar-dark/', views.layout_navbar_dark, name='layout_navbar_dark'),
    path('layout/navbar-sticky/', views.layout_navbar_sticky, name='layout_navbar_sticky'),
    path('layout/navbar-overlap/', views.layout_navbar_overlap, name='layout_navbar_overlap'),
    path('layout/rtl/', views.layout_rtl, name='layout_rtl'),
    path('layout/fluid/', views.layout_fluid, name='layout_fluid'),
    path('layout/fluid-vertical/', views.layout_fluid_vertical, name='layout_fluid_vertical'),

    path('changelog/', views.changelog, name='changelog'),
    path('profile/', views.profile, name='profile'),
    path('icons/', views.icons, name='icons'),
]
