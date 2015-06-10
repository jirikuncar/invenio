{#
# This file is part of Invenio.
# Copyright (C) 2014, 2015 CERN.
#
# Invenio is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
#}

{% extends "format/record/Default_HTML_detailed_base.tpl" %}

{% block header %}
    {{ record.get('subject.term') | prefix('<div style="padding-left:10px;padding-right:10px">') | suffix('</div><hr/>') }}
    <h2>{{ record.get('title.title') }}</h2>
{% endblock %}

{% block details %}
   {% if record.get('number_of_authors', 0) > 0 %}
    <i class="glyphicon glyphicon-user"></i> by
    {% set authors = record.get('authors[:].full_name', []) %}
    {% set sep = joiner("; ") %}
    {% set number_of_displayed_authors = 25 %}
    {% for full_name in authors[0:number_of_displayed_authors] %} {{ sep() }}
      <a href="{{ url_for('search.search', p='author:"' + full_name + '"') }}">
        {{ full_name }}
      </a>
    {% endfor %}
    {% if record.get('number_of_authors', 0) > number_of_displayed_authors %}
    {{ sep() }}
    <a href="#authors_{{ record['recid'] }}"
       class="text-muted" data-toggle="modal"
       data-target="#authors_{{ record['recid'] }}">
        <em> {{ _('et al') }}</em>
    </a>
    {% endif %}
    {% endif %}
    {# bfe_authors(bfo, suffix="<br />", limit="25", interactive="yes", print_affiliations="yes", affiliation_prefix="<small> (", affiliation_suffix=")</small>") #}
    {# bfe_addresses(bfo) #}
    {# bfe_affiliation(bfo) #}
    {# bfe_date(bfo, prefix="<br />", suffix="<br />") #}
    {# bfe_publisher(bfo, prefix="<small>", suffix="</small>") #}
    {# bfe_place(bfo, prefix="<small>", suffix="</small>") #}
    {# bfe_isbn(bfo, prefix="<br />ISBN: ") #}
{% endblock %}

{% block abstract %}
    {{ record.get('abstract.summary')|prefix('<strong>' + _('Abstract:') + ' </strong>')  }}

    {% if record['keywords']|length %}
      <strong><i class="glyphicon glyphicon-tag"></i> {{ _('Keyword(s)')}}: </strong>
      {% for keyword in record['keywords'] %}
      <span class="label label-default">
        <a href="{{ url_for('search.search', p='keyword:' + keyword['term']) }}">
          {{ keyword['term'] }}
        </a>
      </span>
      &nbsp;
    {% endfor %}
    {% endif %}

    {# bfe_notes(bfo, note_prefix="<br /><small><strong>Note: </strong>", note_suffix=" </small>", suffix="<br />") #}

    {# bfe_publi_info(bfo, prefix="<br /><br /><strong>Published in: </strong>") #}<br />
    {# bfe_doi(bfo, prefix="<small><strong>DOI: </strong>", suffix=" </small><br />") #}

    {# bfe_plots(bfo, width="200px", caption="no") #}
{% endblock %}

{% block footer %}
    {# bfe_appears_in_collections(bfo, prefix="<p style='margin-left: 10px;'><em>The record appears in these collections:</em><br />", suffix="</p>") #}

    {# tfn_get_back_to_search_links(record.get('recid'))|wrap(prefix='<div class="pull-right linksbox">', suffix='</div>') #}
{% endblock %}
