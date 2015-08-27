from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^home_page/$', views.landing, name='home_page'),
    url(r'^total_clues/$', views.clues_count, name='total_clues'),
    url(r'^puzzles_lt_10_clues/$', views.puzzles_with_10_or_less, name='puzzles_lt_10_clues'),
    url(r'^devlish_puzzles/$', views.devlish_puzzles, name='devlish_puzzles'),
    url(r'^puzzles_not_10_x_10/$', views.puzzles_not_10x10, name='puzzles_not_10_x_10'),
    url(r'^puzzles_that_use_a_clue/$', views.puzzles_from_given_clue, name='puzzles_that_use_a_clue'),
    url(r'^puzzles/$', views.test_puzzles, name='puzzles'),
    url(r'^clues/$', views.puzzles_with_10_or_less_same_template, name='puzzles_lt_10_clues_same_template'),
    url(r'^clues/$', views.devlish_puzzles_same_template, name='devlish_puzzles_same_template'),
    url(r'^puzzles/$', views.puzzles_not_10x10_st, name='puzzles_not_10_x_10_same_template'),
    url(r'^puzzles/$', views.puzzles_from_given_clue_st, name='puzzles_that_use_a_clue_same_template'),
    url(r'^template_fun/$', views.template_fun, name='template_fun'),
    url(r'^monday_challenge/$', views.monday_challenge, name='monday_challenge'),
]