# -*- coding: utf-8 -*-
import distutils.sysconfig
from os.path import join

from invenio.version import __version__
from invenio.utils.shell import which

EXTENSIONS = [
    'invenio.ext.confighacks',
    'invenio.ext.jinja2hacks',
    'invenio.ext.debug_toolbar',
    'invenio.ext.babel',
    'invenio.ext.sqlalchemy',
    'invenio.ext.sslify',
    'invenio.ext.cache',
    'invenio.ext.session',
    'invenio.ext.login',
    'invenio.ext.principal',
    'invenio.ext.email',
    'invenio.ext.legacy',
    'invenio.ext.assets',
    'invenio.ext.template',
    'invenio.ext.admin',
    'invenio.ext.logging',
    'invenio.ext.gravatar',
    'invenio.ext.collect',
    'invenio.ext.restful',
    'flask.ext.menu:Menu',
    'flask.ext.breadcrumbs:Breadcrumbs',
    'invenio.modules.deposit.url_converters',
]

PACKAGES = [
    'invenio.modules.*'
]

PACKAGES_EXCLUDE = [
    'invenio.modules.communities'
]

CFG_PREFIX = distutils.sysconfig.get_config_var("prefix")

CFG_BATCHUPLOADER_DAEMON_DIR = join(CFG_PREFIX, "var/batchupload")
CFG_BIBDOCFILE_FILEDIR = join(CFG_PREFIX, "var/data/files")
CFG_BINDIR = join(CFG_PREFIX, "bin")
CFG_CACHEDIR = join(CFG_PREFIX, "var/cache")
CFG_ETCDIR = join(CFG_PREFIX, "etc")
CFG_LOCALEDIR = join(CFG_PREFIX, "share/locale")
CFG_LOGDIR = join(CFG_PREFIX, "var/log")
CFG_PYLIBDIR = join(CFG_PREFIX, "lib/python")
CFG_TMPDIR = join(CFG_PREFIX, "var/tmp")
CFG_TMPSHAREDDIR = join(CFG_PREFIX, "var/tmp-shared")
CFG_WEBDIR = join(CFG_PREFIX, "var/www")
CFG_WEBSUBMIT_BIBCONVERTCONFIGDIR = join(CFG_PREFIX, "etc/bibconvert/config")
CFG_WEBSUBMIT_COUNTERSDIR = join(CFG_PREFIX, "var/data/submit/counters")
CFG_WEBSUBMIT_STORAGEDIR = join(CFG_PREFIX, "var/data/submit/storage")


#FIXME check the usage and replace by SQLALCHEMY_URL
CFG_DATABASE_HOST = "localhost"
CFG_DATABASE_NAME = "invenio"
CFG_DATABASE_PASS = "my123p$ss"
CFG_DATABASE_PORT = 3306
CFG_DATABASE_SLAVE = None
CFG_DATABASE_TYPE = "mysql"
CFG_DATABASE_USER = "invenio"

# CFG_FLASK_CACHE_TYPE has been deprecated.
CACHE_TYPE = "redis"

# DO NOT EDIT THIS FILE!  IT WAS AUTOMATICALLY GENERATED
# FROM INVENIO.CONF BY EXECUTING:
# inveniocfg --update-all
CFG_SITE_NAME_INTL = {}
CFG_SITE_NAME_INTL['af'] = "Atlantis Instituut van Fiktiewe Wetenskap"
CFG_SITE_NAME_INTL['ar'] = "معهد أطلنطيس للعلوم الافتراضية"
CFG_SITE_NAME_INTL['bg'] = "Институт за фиктивни науки Атлантис"
CFG_SITE_NAME_INTL['ca'] = "Institut Atlantis de Ciència Fictícia"
CFG_SITE_NAME_INTL['cs'] = "Atlantis Institut Fiktivních Věd"
CFG_SITE_NAME_INTL['de'] = "Atlantis Institut der fiktiven Wissenschaft"
CFG_SITE_NAME_INTL['el'] = "Ινστιτούτο Φανταστικών Επιστημών Ατλαντίδος"
CFG_SITE_NAME_INTL['en'] = "Atlantis Institute of Fictive Science"
CFG_SITE_NAME_INTL['es'] = "Atlantis Instituto de la Ciencia Fictive"
CFG_SITE_NAME_INTL['fr'] = "Atlantis Institut des Sciences Fictives"
CFG_SITE_NAME_INTL['hr'] = "Institut Fiktivnih Znanosti Atlantis"
CFG_SITE_NAME_INTL['gl'] = "Instituto Atlantis de Ciencia Fictive"
CFG_SITE_NAME_INTL['ka'] = "ატლანტიდის ფიქტიური მეცნიერების ინსტიტუტი"
CFG_SITE_NAME_INTL['it'] = "Atlantis Istituto di Scienza Fittizia"
CFG_SITE_NAME_INTL['rw'] = "Atlantis Ishuri Rikuru Ry'ubuhanga"
CFG_SITE_NAME_INTL['lt'] = "Fiktyvių Mokslų Institutas Atlantis"
CFG_SITE_NAME_INTL['hu'] = "Kitalált Tudományok Atlantiszi Intézete"
CFG_SITE_NAME_INTL['ja'] = "Fictive 科学のAtlantis の協会"
CFG_SITE_NAME_INTL['no'] = "Atlantis Institutt for Fiktiv Vitenskap"
CFG_SITE_NAME_INTL['pl'] = "Instytut Fikcyjnej Nauki Atlantis"
CFG_SITE_NAME_INTL['pt'] = "Instituto Atlantis de Ciência Fictícia"
CFG_SITE_NAME_INTL['ro'] = "Institutul Atlantis al Ştiinţelor Fictive"
CFG_SITE_NAME_INTL['ru'] = "Институт Фиктивных Наук Атлантиды"
CFG_SITE_NAME_INTL['sk'] = "Atlantis Inštitút Fiktívnych Vied"
CFG_SITE_NAME_INTL['sv'] = "Atlantis Institut för Fiktiv Vetenskap"
CFG_SITE_NAME_INTL['uk'] = "Інститут вигаданих наук в Атлантісі"
CFG_SITE_NAME_INTL['zh_CN'] = "阿特兰提斯虚拟科学学院"
CFG_SITE_NAME_INTL['zh_TW'] = "阿特蘭提斯虛擬科學學院"
CFG_ACCESS_CONTROL_LEVEL_ACCOUNTS = 0
CFG_ACCESS_CONTROL_LEVEL_GUESTS = 0
CFG_ACCESS_CONTROL_LEVEL_SITE = 0
CFG_ACCESS_CONTROL_LIMIT_REGISTRATION_TO_DOMAIN = ""
CFG_ACCESS_CONTROL_NOTIFY_ADMIN_ABOUT_NEW_ACCOUNTS = 0
CFG_ACCESS_CONTROL_NOTIFY_USER_ABOUT_ACTIVATION = 0
CFG_ACCESS_CONTROL_NOTIFY_USER_ABOUT_DELETION = 0
CFG_ACCESS_CONTROL_NOTIFY_USER_ABOUT_NEW_ACCOUNT = 1
CFG_ADS_SITE = 0
CFG_APACHE_GROUP_FILE = "demo-site-apache-user-groups"
CFG_APACHE_PASSWORD_FILE = "demo-site-apache-user-passwords"
CFG_BATCHUPLOADER_FILENAME_MATCHING_POLICY = ['reportnumber', 'recid', ]
CFG_BATCHUPLOADER_WEB_ROBOT_AGENTS = r"invenio_webupload|Invenio-.*"
CFG_BATCHUPLOADER_WEB_ROBOT_RIGHTS = {
'127.0.0.1': ['*'], # useful for testing
'127.0.1.1': ['*'], # useful for testing
'10.0.0.1': ['BOOK', 'REPORT'], # Example 1
'10.0.0.2': ['POETRY', 'PREPRINT'], # Example 2
}
CFG_BIBAUTHORID_AUTHOR_TICKET_ADMIN_EMAIL = "info@invenio-software.org"
CFG_BIBAUTHORID_ENABLED = True
CFG_BIBAUTHORID_EXTERNAL_CLAIMED_RECORDS_KEY = []
CFG_BIBAUTHORID_MAX_PROCESSES = 12
CFG_BIBAUTHORID_ON_AUTHORPAGES = True
CFG_BIBAUTHORID_PERSONID_SQL_MAX_THREADS = 12
CFG_BIBAUTHORID_UI_SKIP_ARXIV_STUB_PAGE = False
CFG_BIBCATALOG_SYSTEM = "EMAIL"
CFG_BIBCATALOG_SYSTEM_EMAIL_ADDRESS = "info@invenio-software.org"
CFG_BIBCATALOG_SYSTEM_RT_CLI = "/usr/bin/rt"
CFG_BIBCATALOG_SYSTEM_RT_DEFAULT_PWD = ""
CFG_BIBCATALOG_SYSTEM_RT_DEFAULT_USER = ""
CFG_BIBCATALOG_SYSTEM_RT_URL = "http://localhost/rt3"
CFG_BIBCIRCULATION_ACQ_STATUS_CANCELLED = "cancelled"
CFG_BIBCIRCULATION_ACQ_STATUS_NEW = "new"
CFG_BIBCIRCULATION_ACQ_STATUS_ON_ORDER = "on order"
CFG_BIBCIRCULATION_ACQ_STATUS_PARTIAL_RECEIPT = "partial receipt"
CFG_BIBCIRCULATION_ACQ_STATUS_RECEIVED = "received"
CFG_BIBCIRCULATION_AMAZON_ACCESS_KEY = ""
CFG_BIBCIRCULATION_ILL_STATUS_CANCELLED = "cancelled"
CFG_BIBCIRCULATION_ILL_STATUS_NEW = "new"
CFG_BIBCIRCULATION_ILL_STATUS_ON_LOAN = "on loan"
CFG_BIBCIRCULATION_ILL_STATUS_RECEIVED = "received"
CFG_BIBCIRCULATION_ILL_STATUS_REQUESTED = "requested"
CFG_BIBCIRCULATION_ILL_STATUS_RETURNED = "returned"
CFG_BIBCIRCULATION_ITEM_STATUS_CANCELLED = "cancelled"
CFG_BIBCIRCULATION_ITEM_STATUS_CLAIMED = "claimed"
CFG_BIBCIRCULATION_ITEM_STATUS_IN_PROCESS = "in process"
CFG_BIBCIRCULATION_ITEM_STATUS_NOT_ARRIVED = "not arrived"
CFG_BIBCIRCULATION_ITEM_STATUS_ON_LOAN = "on loan"
CFG_BIBCIRCULATION_ITEM_STATUS_ON_ORDER = "on order"
CFG_BIBCIRCULATION_ITEM_STATUS_ON_SHELF = "on shelf"
CFG_BIBCIRCULATION_ITEM_STATUS_OPTIONAL = []
CFG_BIBCIRCULATION_ITEM_STATUS_UNDER_REVIEW = "under review"
CFG_BIBCIRCULATION_LIBRARY_TYPE_EXTERNAL = "external"
CFG_BIBCIRCULATION_LIBRARY_TYPE_HIDDEN = "hidden"
CFG_BIBCIRCULATION_LIBRARY_TYPE_INTERNAL = "internal"
CFG_BIBCIRCULATION_LIBRARY_TYPE_MAIN = "main"
CFG_BIBCIRCULATION_LOAN_STATUS_EXPIRED = "expired"
CFG_BIBCIRCULATION_LOAN_STATUS_ON_LOAN = "on loan"
CFG_BIBCIRCULATION_LOAN_STATUS_RETURNED = "returned"
CFG_BIBCIRCULATION_PROPOSAL_STATUS_NEW = "proposal-new"
CFG_BIBCIRCULATION_PROPOSAL_STATUS_ON_ORDER = "proposal-on order"
CFG_BIBCIRCULATION_PROPOSAL_STATUS_PUT_ASIDE = "proposal-put aside"
CFG_BIBCIRCULATION_PROPOSAL_STATUS_RECEIVED = "proposal-received"
CFG_BIBCIRCULATION_REQUEST_STATUS_CANCELLED = "cancelled"
CFG_BIBCIRCULATION_REQUEST_STATUS_DONE = "done"
CFG_BIBCIRCULATION_REQUEST_STATUS_PENDING = "pending"
CFG_BIBCIRCULATION_REQUEST_STATUS_PROPOSED = "proposed"
CFG_BIBCIRCULATION_REQUEST_STATUS_WAITING = "waiting"
CFG_BIBCLASSIFY_WEB_MAXKW = 100
CFG_BIBDOCFILE_ADDITIONAL_KNOWN_FILE_EXTENSIONS = ['hpg', 'link', 'lis', 'llb', 'mat', 'mpp', 'msg', 'docx', 'docm', 'xlsx', 'xlsm', 'xlsb', 'pptx', 'pptm', 'ppsx', 'ppsm', ]
CFG_BIBDOCFILE_ADDITIONAL_KNOWN_MIMETYPES = {
"application/xml-dtd": ".dtd",
}
CFG_BIBDOCFILE_BEST_FORMATS_TO_EXTRACT_TEXT_FROM = ('txt', 'html', 'xml', 'odt', 'doc', 'docx', 'djvu', 'pdf', 'ps', 'ps.gz')
CFG_BIBDOCFILE_DESIRED_CONVERSIONS = {
'pdf' : ('pdf;pdfa', ),
'ps.gz' : ('pdf;pdfa', ),
'djvu' : ('pdf', ),
'sxw': ('doc', 'odt', 'pdf;pdfa', ),
'docx' : ('doc', 'odt', 'pdf;pdfa', ),
'doc' : ('odt', 'pdf;pdfa', 'docx'),
'rtf' : ('pdf;pdfa', 'odt', ),
'odt' : ('pdf;pdfa', 'doc', ),
'pptx' : ('ppt', 'odp', 'pdf;pdfa', ),
'ppt' : ('odp', 'pdf;pdfa', 'pptx'),
'sxi': ('odp', 'pdf;pdfa', ),
'odp' : ('pdf;pdfa', 'ppt', ),
'xlsx' : ('xls', 'ods', 'csv'),
'xls' : ('ods', 'csv'),
'ods' : ('xls', 'xlsx', 'csv'),
'sxc': ('xls', 'xlsx', 'csv'),
'tiff' : ('pdf;pdfa', ),
'tif' : ('pdf;pdfa', ),}
CFG_BIBDOCFILE_DOCUMENT_FILE_MANAGER_DOCTYPES = [
('Main', 'Main document'),
('LaTeX', 'LaTeX'),
('Source', 'Source'),
('Additional', 'Additional File'),
('Audio', 'Audio file'),
('Video', 'Video file'),
('Script', 'Script'),
('Data', 'Data'),
('Figure', 'Figure'),
('Schema', 'Schema'),
('Graph', 'Graph'),
('Image', 'Image'),
('Drawing', 'Drawing'),
('Slides', 'Slides')]
CFG_BIBDOCFILE_DOCUMENT_FILE_MANAGER_MISC = {
'can_revise_doctypes': ['*'],
'can_comment_doctypes': ['*'],
'can_describe_doctypes': ['*'],
'can_delete_doctypes': ['*'],
'can_keep_doctypes': ['*'],
'can_rename_doctypes': ['*'],
'can_add_format_to_doctypes': ['*'],
'can_restrict_doctypes': ['*'],
}
CFG_BIBDOCFILE_DOCUMENT_FILE_MANAGER_RESTRICTIONS = [
('', 'Public'),
('restricted', 'Restricted')]
CFG_BIBDOCFILE_ENABLE_BIBDOCFSINFO_CACHE = 0
CFG_BIBDOCFILE_FILESYSTEM_BIBDOC_GROUP_LIMIT = 5000
CFG_BIBDOCFILE_MD5_CHECK_PROBABILITY = 0.1
CFG_BIBDOCFILE_USE_XSENDFILE = 0
CFG_BIBEDIT_AUTOCOMPLETE_INSTITUTIONS_FIELDS = ['100__u', '700__u', '701__u', '502__c', ]
CFG_BIBEDIT_EXTEND_RECORD_WITH_COLLECTION_TEMPLATE = { 'POETRY' : 'record_poem'}
CFG_BIBEDIT_KB_INSTITUTIONS = "InstitutionsCollection"
CFG_BIBEDIT_KB_SUBJECTS = "Subjects"
CFG_BIBEDIT_LOCKLEVEL = 3
CFG_BIBEDIT_PROTECTED_FIELDS = ""
CFG_BIBEDIT_QUEUE_CHECK_METHOD = "bibrecord"
CFG_BIBEDIT_TIMEOUT = 3600
CFG_BIBEDITMULTI_LIMIT_DELAYED_PROCESSING = 20000
CFG_BIBEDITMULTI_LIMIT_DELAYED_PROCESSING_TIME = "22:00-05:00"
CFG_BIBEDITMULTI_LIMIT_INSTANT_PROCESSING = 2000
CFG_BIBFIELD_MASTER_FORMATS = ['marc', ]
CFG_BIBFORMAT_ADDTHIS_ID = ""
CFG_BIBFORMAT_DISABLE_I18N_FOR_CACHED_FORMATS = []
CFG_BIBFORMAT_HIDDEN_FILE_FORMATS = []
CFG_BIBFORMAT_HIDDEN_TAGS = ['595', ]
CFG_BIBINDEX_AUTHOR_WORD_INDEX_EXCLUDE_FIRST_NAMES = False
CFG_BIBINDEX_CHARS_ALPHANUMERIC_SEPARATORS = r"[\!\"\#\$\%\&\'\(\)\*\+\,\-\.\/\:\;\<\=\>\?\@\[\\\]\^\_\`\{\|\}\~]"
CFG_BIBINDEX_CHARS_PUNCTUATION = r"[\.\,\:\;\?\!\"]"
CFG_BIBINDEX_FULLTEXT_INDEX_LOCAL_FILES_ONLY = 1
CFG_BIBINDEX_MIN_WORD_LENGTH = 0
CFG_BIBINDEX_PATH_TO_STOPWORDS_FILE = "etc/bibrank/stopwords.kb"
CFG_BIBINDEX_PERFORM_OCR_ON_DOCNAMES = r"scan-.*"
CFG_BIBINDEX_REMOVE_HTML_MARKUP = 0
CFG_BIBINDEX_REMOVE_LATEX_MARKUP = 0
CFG_BIBINDEX_REMOVE_STOPWORDS = 0
CFG_BIBINDEX_SPLASH_PAGES = {
"http://documents\.cern\.ch/setlink\?.*": ".*",
"http://ilcagenda\.linearcollider\.org/subContributionDisplay\.py\?.*|http://ilcagenda\.linearcollider\.org/contributionDisplay\.py\?.*": "http://ilcagenda\.linearcollider\.org/getFile\.py/access\?.*|http://ilcagenda\.linearcollider\.org/materialDisplay\.py\?.*",
}
CFG_BIBINDEX_SYNONYM_KBRS = {
'global': ['INDEX-SYNONYM-TITLE', 'exact'],
'title': ['INDEX-SYNONYM-TITLE', 'exact'],
}
CFG_BIBINDEX_URLOPENER_PASSWORD = "mysuperpass"
CFG_BIBINDEX_URLOPENER_USERNAME = "mysuperuser"
CFG_BIBMATCH_FUZZY_EMPTY_RESULT_LIMIT = 1
CFG_BIBMATCH_FUZZY_MATCH_VALIDATION_LIMIT = 0.65
CFG_BIBMATCH_FUZZY_WORDLIMITS = {
'100__a': 2,
'245__a': 4
}
CFG_BIBMATCH_LOCAL_SLEEPTIME = 0.0
CFG_BIBMATCH_MATCH_VALIDATION_RULESETS = [('default', [{ 'tags' : '245__%,242__%',
'threshold' : 0.8,
'compare_mode' : 'lazy',
'match_mode' : 'title',
'result_mode' : 'normal' },
{ 'tags' : '037__a,088__a',
'threshold' : 1.0,
'compare_mode' : 'lazy',
'match_mode' : 'identifier',
'result_mode' : 'final' },
{ 'tags' : '100__a,700__a',
'threshold' : 0.8,
'compare_mode' : 'normal',
'match_mode' : 'author',
'result_mode' : 'normal' },
{ 'tags' : '773__a',
'threshold' : 1.0,
'compare_mode' : 'lazy',
'match_mode' : 'title',
'result_mode' : 'normal' }]),
('980__ \$\$a(THESIS|Thesis)', [{ 'tags' : '100__a',
'threshold' : 0.8,
'compare_mode' : 'strict',
'match_mode' : 'author',
'result_mode' : 'normal' },
{ 'tags' : '700__a,701__a',
'threshold' : 1.0,
'compare_mode' : 'lazy',
'match_mode' : 'author',
'result_mode' : 'normal' },
{ 'tags' : '100__a,700__a',
'threshold' : 0.8,
'compare_mode' : 'ignored',
'match_mode' : 'author',
'result_mode' : 'normal' }]),
('260__', [{ 'tags' : '260__c',
'threshold' : 0.8,
'compare_mode' : 'lazy',
'match_mode' : 'date',
'result_mode' : 'normal' }]),
('0247_', [{ 'tags' : '0247_a',
'threshold' : 1.0,
'compare_mode' : 'lazy',
'match_mode' : 'identifier',
'result_mode' : 'final' }]),
('020__', [{ 'tags' : '020__a',
'threshold' : 1.0,
'compare_mode' : 'lazy',
'match_mode' : 'identifier',
'result_mode' : 'joker' }])
]
CFG_BIBMATCH_QUERY_TEMPLATES = {
'title' : '[title]',
'title-author' : '[title] [author]',
'reportnumber' : 'reportnumber:[reportnumber]'
}
CFG_BIBMATCH_REMOTE_SLEEPTIME = 2.0
CFG_BIBMATCH_SEARCH_RESULT_MATCH_LIMIT = 15
CFG_BIBRANK_SELFCITES_PRECOMPUTE = 0
CFG_BIBRANK_SELFCITES_USE_BIBAUTHORID = 0
CFG_BIBRANK_SHOW_CITATION_GRAPHS = 1
CFG_BIBRANK_SHOW_CITATION_LINKS = 1
CFG_BIBRANK_SHOW_CITATION_STATS = 1
CFG_BIBRANK_SHOW_DOWNLOAD_GRAPHS = 1
CFG_BIBRANK_SHOW_DOWNLOAD_GRAPHS_CLIENT_IP_DISTRIBUTION = 0
CFG_BIBRANK_SHOW_DOWNLOAD_STATS = 1
CFG_BIBRANK_SHOW_READING_STATS = 1
CFG_BIBSCHED_EDITOR = which("vim")
CFG_BIBSCHED_GC_TASKS_OLDER_THAN = 30
CFG_BIBSCHED_GC_TASKS_TO_ARCHIVE = ['bibupload', 'oairepositoryupdater', ]
CFG_BIBSCHED_GC_TASKS_TO_REMOVE = ['bibindex', 'bibreformat', 'webcoll', 'bibrank', 'inveniogc', ]
CFG_BIBSCHED_LOG_PAGER = which("less")
CFG_BIBSCHED_MAX_ARCHIVED_ROWS_DISPLAY = 500
CFG_BIBSCHED_MAX_NUMBER_CONCURRENT_TASKS = 1
CFG_BIBSCHED_NODE_TASKS = {}
CFG_BIBSCHED_PROCESS_USER = ""
CFG_BIBSCHED_REFRESHTIME = 5
CFG_BIBSORT_BUCKETS = 1
CFG_BIBUPLOAD_CONFLICTING_REVISION_TICKET_QUEUE = ""
CFG_BIBUPLOAD_CONTROLLED_PROVENANCE_TAGS = ['6531_9', ]
CFG_BIBUPLOAD_DELETE_FORMATS = ['hb', ]
CFG_BIBUPLOAD_DISABLE_RECORD_REVISIONS = 0
CFG_BIBUPLOAD_EXTERNAL_OAIID_PROVENANCE_TAG = "035__9"
CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG = "035__a"
CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG = "970__a"
CFG_BIBUPLOAD_FFT_ALLOWED_EXTERNAL_URLS = [
('http(s)?://.*', {}),
]
CFG_BIBUPLOAD_FFT_ALLOWED_LOCAL_PATHS = ['/tmp', '/home', ]
CFG_BIBUPLOAD_REFERENCE_TAG = "999"
CFG_BIBUPLOAD_SERIALIZE_RECORD_STRUCTURE = 1
CFG_BIBUPLOAD_STRONG_TAGS = ['964', ]
CFG_BIBWORKFLOW_WORKER = "worker_celery"
CFG_BROKER_URL = "amqp://guest@localhost:5672//"
CFG_CELERY_RESULT_BACKEND = "amqp"
CFG_CERN_SITE = 0
CFG_ORGANIZATION_IDENTIFIER = ""
CFG_CROSSREF_PASSWORD = ""
CFG_CROSSREF_USERNAME = ""
CFG_DEVEL_SITE = 0
CFG_DEVEL_TEST_DATABASE_ENGINES = {}
CFG_DEVEL_TOOLS = []
CFG_EMAIL_BACKEND = "flask.ext.email.backends.smtp.Mail"
CFG_ERRORLIB_RESET_EXCEPTION_NOTIFICATION_COUNTER_AFTER = 14400
CFG_FLASK_DISABLED_BLUEPRINTS = []
CFG_FLASK_SERVE_STATIC_FILES = 1
CFG_INSPIRE_SITE = 0
CFG_INTBITSET_ENABLE_SANITY_CHECKS = False
CFG_JSTESTDRIVER_PORT = 9876
CFG_MATHJAX_HOSTING = "local"
CFG_MISCUTIL_DEFAULT_PROCESS_TIMEOUT = 300
CFG_MISCUTIL_SMTP_HOST = "localhost"
CFG_MISCUTIL_SMTP_PASS = ""
CFG_MISCUTIL_SMTP_PORT = 25
CFG_MISCUTIL_SMTP_TLS = False
CFG_MISCUTIL_SMTP_USER = ""
CFG_MISCUTIL_SQL_RUN_SQL_MANY_LIMIT = 10000
CFG_MISCUTIL_SQL_USE_SQLALCHEMY = False
CFG_OAI_DELETED_POLICY = "persistent"
CFG_OAI_EXPIRE = 90000
CFG_OAI_FAILED_HARVESTING_EMAILS_ADMIN = True
CFG_OAI_FAILED_HARVESTING_STOP_QUEUE = 1
CFG_OAI_FRIENDS = ['http://cds.cern.ch/oai2d', 'http://openaire.cern.ch/oai2d', 'http://export.arxiv.org/oai2', ]
CFG_OAI_ID_FIELD = "909COo"
CFG_OAI_ID_PREFIX = "atlantis.cern.ch"
CFG_OAI_IDENTIFY_DESCRIPTION = """<description>
<eprints xmlns="http://www.openarchives.org/OAI/1.1/eprints"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://www.openarchives.org/OAI/1.1/eprints
http://www.openarchives.org/OAI/1.1/eprints.xsd">
<content>
<URL>http://localhost</URL>
</content>
<metadataPolicy>
<text>Free and unlimited use by anybody with obligation to refer to original record</text>
</metadataPolicy>
<dataPolicy>
<text>Full content, i.e. preprints may not be harvested by robots</text>
</dataPolicy>
<submissionPolicy>
<text>Submission restricted. Submitted documents are subject of approval by OAI repository admins.</text>
</submissionPolicy>
</eprints>
</description>"""
CFG_OAI_LICENSE_FIELD = "540__"
CFG_OAI_LICENSE_PUBLISHER_SUBFIELD = "b"
CFG_OAI_LICENSE_TERMS_SUBFIELD = "a"
CFG_OAI_LICENSE_URI_SUBFIELD = "u"
CFG_OAI_LOAD = 500
CFG_OAI_METADATA_FORMATS = {
'marcxml': ('XOAIMARC', 'http://www.openarchives.org/OAI/1.1/dc.xsd', 'http://purl.org/dc/elements/1.1/'),
'oai_dc': ('XOAIDC', 'http://www.loc.gov/standards/marcxml/schema/MARC21slim.xsd', 'http://www.loc.gov/MARC21/slim'),
}
CFG_OAI_PREVIOUS_SET_FIELD = "909COq"
CFG_OAI_PROVENANCE_ALTERED_SUBFIELD = "t"
CFG_OAI_PROVENANCE_BASEURL_SUBFIELD = "u"
CFG_OAI_PROVENANCE_DATESTAMP_SUBFIELD = "d"
CFG_OAI_PROVENANCE_HARVESTDATE_SUBFIELD = "h"
CFG_OAI_PROVENANCE_METADATANAMESPACE_SUBFIELD = "m"
CFG_OAI_PROVENANCE_ORIGINDESCRIPTION_SUBFIELD = "d"
CFG_OAI_RIGHTS_CONTACT_SUBFIELD = "e"
CFG_OAI_RIGHTS_DATE_SUBFIELD = "g"
CFG_OAI_RIGHTS_FIELD = "542__"
CFG_OAI_RIGHTS_HOLDER_SUBFIELD = "d"
CFG_OAI_RIGHTS_STATEMENT_SUBFIELD = "f"
CFG_OAI_RIGHTS_URI_SUBFIELD = "u"
CFG_OAI_SAMPLE_IDENTIFIER = "oai:atlantis.cern.ch:123"
CFG_OAI_SET_FIELD = "909COp"
CFG_OAI_SLEEP = 2
CFG_OAUTH1_CONFIGURATIONS = {}
CFG_OAUTH1_PROVIDERS = []
CFG_OAUTH2_CONFIGURATIONS = {}
CFG_OAUTH2_PROVIDERS = []
CFG_OPENID_CONFIGURATIONS = {}
CFG_OPENID_PROVIDERS = []
CFG_OPENOFFICE_SERVER_HOST = "localhost"
CFG_OPENOFFICE_SERVER_PORT = 2002
CFG_OPENOFFICE_USER = "nobody"
CFG_PATH_ANY2DJVU = ""
CFG_PATH_CONVERT = which("convert")
CFG_PATH_DJVUPS = ""
CFG_PATH_DJVUTXT = ""
CFG_PATH_FFMPEG = ""
CFG_PATH_FFPROBE = ""
CFG_PATH_GFILE = which("file")
CFG_PATH_GS = which("gs")
CFG_PATH_GUNZIP = which("gunzip")
CFG_PATH_GZIP = which("gzip")
CFG_PATH_MD5SUM = ""
CFG_PATH_MEDIAINFO = ""
CFG_PATH_MYSQL = which("mysql")
CFG_PATH_OCROSCRIPT = ""
CFG_PATH_OPENOFFICE_PYTHON = which("python")
CFG_PATH_PAMFILE = which("pdftoppm")
CFG_PATH_PDF2PS = which("pdf2ps")
CFG_PATH_PDFINFO = which("pdfinfo")
CFG_PATH_PDFLATEX = which("pdflatex")
CFG_PATH_PDFOPT = which("pdfopt") or which("cp")
CFG_PATH_PDFTK = ""
CFG_PATH_PDFTOPPM = which("pdftoppm")
CFG_PATH_PDFTOPS = which("pdftops")
CFG_PATH_PDFTOTEXT = which("pdftotext")
CFG_PATH_PHP = which("php")
CFG_PATH_PS2PDF = which("ps2pdf")
CFG_PATH_PSTOASCII = which("ps2ascii")
CFG_PATH_PSTOTEXT = ""
CFG_PATH_TAR = which("tar")
CFG_PATH_TIFF2PDF = which("tiff2pdf")
CFG_PATH_WGET = which("wget")
CFG_PLOTEXTRACTOR_CONTEXT_EXTRACT_LIMIT = 750
CFG_PLOTEXTRACTOR_CONTEXT_SENTENCE_LIMIT = 2
CFG_PLOTEXTRACTOR_CONTEXT_WORD_LIMIT = 75
CFG_PLOTEXTRACTOR_DISALLOWED_TEX = ['begin', 'end', 'section', 'includegraphics', 'caption', 'acknowledgements', ]
CFG_PLOTEXTRACTOR_DOWNLOAD_TIMEOUT = 2.0
CFG_PLOTEXTRACTOR_SOURCE_BASE_URL = "http://arxiv.org/"
CFG_PLOTEXTRACTOR_SOURCE_PDF_FOLDER = "pdf/"
CFG_PLOTEXTRACTOR_SOURCE_TARBALL_FOLDER = "e-print/"
CFG_REFEXTRACT_KBS_OVERRIDE = {}
CFG_REFEXTRACT_TICKET_QUEUE = None
CFG_SITE_ADMIN_EMAIL = "info@invenio-software.org"
CFG_SITE_ADMIN_EMAIL_EXCEPTIONS = 1
CFG_SITE_EMERGENCY_EMAIL_ADDRESSES = {}
CFG_SITE_LANG = "en"
CFG_SITE_LANGS = ['af', 'ar', 'bg', 'ca', 'cs', 'de', 'el', 'en', 'es', 'fr', 'hr', 'gl', 'ka', 'it', 'rw', 'lt', 'hu', 'ja', 'no', 'pl', 'pt', 'ro', 'ru', 'sk', 'sv', 'uk', 'zh_CN', 'zh_TW', ]
CFG_SITE_NAME = "Atlantis Institute of Fictive Science"
CFG_SITE_RECORD = "record"
SECRET_KEY = "change_me"
CFG_SITE_SECURE_URL = "http://localhost:4000"
CFG_SITE_SUPPORT_EMAIL = "info@invenio-software.org"
CFG_SITE_URL = "http://localhost:4000"
CFG_SOLR_URL = ""
CFG_VERSION = __version__
CFG_WEB_API_KEY_ALLOWED_URL = []
CFG_WEBALERT_ALERT_ENGINE_EMAIL = "info@invenio-software.org"
CFG_WEBALERT_MAX_NUM_OF_CHARS_PER_LINE_IN_ALERT_EMAIL = 72
CFG_WEBALERT_MAX_NUM_OF_RECORDS_IN_ALERT_EMAIL = 20
CFG_WEBALERT_SEND_EMAIL_NUMBER_OF_TRIES = 3
CFG_WEBALERT_SEND_EMAIL_SLEEPTIME_BETWEEN_TRIES = 300
CFG_WEBAUTHORPROFILE_CACHE_EXPIRED_DELAY_BIBSCHED = 5
CFG_WEBAUTHORPROFILE_CACHE_EXPIRED_DELAY_LIVE = 7
CFG_WEBAUTHORPROFILE_MAX_AFF_LIST = 100
CFG_WEBAUTHORPROFILE_MAX_COAUTHOR_LIST = 100
CFG_WEBAUTHORPROFILE_MAX_COLLAB_LIST = 100
CFG_WEBAUTHORPROFILE_MAX_HEP_CHOICES = 10
CFG_WEBAUTHORPROFILE_MAX_KEYWORD_LIST = 100
CFG_WEBAUTHORPROFILE_USE_BIBAUTHORID = False
CFG_WEBBASKET_MAX_NUMBER_OF_DISPLAYED_BASKETS = 20
CFG_WEBBASKET_USE_RICH_TEXT_EDITOR = False
CFG_WEBCOMMENT_ADMIN_NOTIFICATION_LEVEL = 1
CFG_WEBCOMMENT_ALERT_ENGINE_EMAIL = "info@invenio-software.org"
CFG_WEBCOMMENT_ALLOW_COMMENTS = 1
CFG_WEBCOMMENT_ALLOW_REVIEWS = 1
CFG_WEBCOMMENT_ALLOW_SHORT_REVIEWS = 0
CFG_WEBCOMMENT_AUTHOR_DELETE_COMMENT_OPTION = 1
CFG_WEBCOMMENT_DEFAULT_MODERATOR = "info@invenio-software.org"
CFG_WEBCOMMENT_EMAIL_REPLIES_TO = {
'Articles': ['506__d', '506__m'],
}
CFG_WEBCOMMENT_MAX_ATTACHED_FILES = 5
CFG_WEBCOMMENT_MAX_ATTACHMENT_SIZE = 5242880
CFG_WEBCOMMENT_MAX_COMMENT_THREAD_DEPTH = 1
CFG_WEBCOMMENT_NB_COMMENTS_IN_DETAILED_VIEW = 1
CFG_WEBCOMMENT_NB_REPORTS_BEFORE_SEND_EMAIL_TO_ADMIN = 5
CFG_WEBCOMMENT_NB_REVIEWS_IN_DETAILED_VIEW = 1
CFG_WEBCOMMENT_RESTRICTION_DATAFIELD = {
'Articles': '5061_a',
'Pictures': '5061_a',
'Theses': '5061_a',
}
CFG_WEBCOMMENT_ROUND_DATAFIELD = {
'Articles': '562__c',
'Pictures': '562__c',
}
CFG_WEBCOMMENT_TIMELIMIT_PROCESSING_COMMENTS_IN_SECONDS = 20
CFG_WEBCOMMENT_TIMELIMIT_PROCESSING_REVIEWS_IN_SECONDS = 20
CFG_WEBCOMMENT_USE_MATHJAX_IN_COMMENTS = 1
CFG_WEBCOMMENT_USE_RICH_TEXT_EDITOR = False
CFG_WEBDEPOSIT_MAX_UPLOAD_SIZE = 104857600
CFG_WEBDEPOSIT_UPLOAD_FOLDER = "var/tmp/webdeposit_uploads"
CFG_WEBLINKBACK_TRACKBACK_ENABLED = 0
CFG_WEBMESSAGE_DAYS_BEFORE_DELETE_ORPHANS = 60
CFG_WEBMESSAGE_MAX_NB_OF_MESSAGES = 30
CFG_WEBMESSAGE_MAX_SIZE_OF_MESSAGE = 20000
CFG_WEBSEARCH_ADVANCEDSEARCH_PATTERN_BOX_WIDTH = 30
CFG_WEBSEARCH_AUTHOR_ET_AL_THRESHOLD = 3
CFG_WEBSEARCH_CALL_BIBFORMAT = 0
CFG_WEBSEARCH_CITESUMMARY_SELFCITES_THRESHOLD = 2000
CFG_WEBSEARCH_CREATE_SIMILARLY_NAMED_AUTHORS_LINK_BOX = 1
CFG_WEBSEARCH_DEF_RECORDS_IN_GROUPS = 10
CFG_WEBSEARCH_DETAILED_META_FORMAT = "hdm"
CFG_WEBSEARCH_DISPLAY_NEAREST_TERMS = 1
CFG_WEBSEARCH_ENABLE_GOOGLESCHOLAR = True
CFG_WEBSEARCH_ENABLE_OPENGRAPH = False
CFG_WEBSEARCH_EXTERNAL_COLLECTION_SEARCH_MAXRESULTS = 10
CFG_WEBSEARCH_EXTERNAL_COLLECTION_SEARCH_TIMEOUT = 5
CFG_WEBSEARCH_FIELDS_CONVERT = {}
CFG_WEBSEARCH_FULLTEXT_SNIPPETS = {
'': 4,
}
CFG_WEBSEARCH_FULLTEXT_SNIPPETS_CHARS = {
'': 100,
}
CFG_WEBSEARCH_FULLTEXT_SNIPPETS_GENERATOR = "native"
CFG_WEBSEARCH_I18N_LATEST_ADDITIONS = 0
CFG_WEBSEARCH_INSTANT_BROWSE = 10
CFG_WEBSEARCH_INSTANT_BROWSE_RSS = 25
CFG_WEBSEARCH_LIGHTSEARCH_PATTERN_BOX_WIDTH = 60
CFG_WEBSEARCH_MAX_RECORDS_IN_GROUPS = 200
CFG_WEBSEARCH_NARROW_SEARCH_SHOW_GRANDSONS = 1
CFG_WEBSEARCH_NB_RECORDS_TO_SORT = 1000
CFG_WEBSEARCH_PREV_NEXT_HIT_FOR_GUESTS = 1
CFG_WEBSEARCH_PREV_NEXT_HIT_LIMIT = 1000
CFG_WEBSEARCH_RSS_I18N_COLLECTIONS = []
CFG_WEBSEARCH_RSS_MAX_CACHED_REQUESTS = 1000
CFG_WEBSEARCH_RSS_TTL = 360
CFG_WEBSEARCH_SEARCH_CACHE_SIZE = 1
CFG_WEBSEARCH_SEARCH_CACHE_TIMEOUT = 600
CFG_WEBSEARCH_SHOW_COMMENT_COUNT = 1
CFG_WEBSEARCH_SHOW_REVIEW_COUNT = 1
CFG_WEBSEARCH_SIMPLESEARCH_PATTERN_BOX_WIDTH = 40
CFG_WEBSEARCH_SPIRES_SYNTAX = 1
CFG_WEBSEARCH_SPLIT_BY_COLLECTION = 1
CFG_WEBSEARCH_SYNONYM_KBRS = {
'journal': ['SEARCH-SYNONYM-JOURNAL', 'leading_to_number'],
}
CFG_WEBSEARCH_USE_ALEPH_SYSNOS = 0
CFG_WEBSEARCH_USE_MATHJAX_FOR_FORMATS = []
CFG_WEBSEARCH_VIEWRESTRCOLL_POLICY = "ANY"
CFG_WEBSEARCH_WILDCARD_LIMIT = 50000
CFG_WEBSESSION_ADDRESS_ACTIVATION_EXPIRE_IN_DAYS = 3
CFG_WEBSESSION_DIFFERENTIATE_BETWEEN_GUESTS = 0
CFG_WEBSESSION_EXPIRY_LIMIT_DEFAULT = 2
CFG_WEBSESSION_EXPIRY_LIMIT_REMEMBER = 365
CFG_WEBSESSION_IPADDR_CHECK_SKIP_BITS = 0
CFG_WEBSESSION_NOT_CONFIRMED_EMAIL_ADDRESS_EXPIRE_IN_DAYS = 10
CFG_WEBSESSION_RESET_PASSWORD_EXPIRE_IN_DAYS = 3
CFG_WEBSTAT_BIBCIRCULATION_START_YEAR = ""
CFG_WEBSTYLE_CDSPAGEBOXLEFTBOTTOM = ""
CFG_WEBSTYLE_CDSPAGEBOXLEFTTOP = ""
CFG_WEBSTYLE_CDSPAGEBOXRIGHTBOTTOM = ""
CFG_WEBSTYLE_CDSPAGEBOXRIGHTTOP = ""
CFG_WEBSTYLE_EMAIL_ADDRESSES_OBFUSCATION_MODE = 2
CFG_WEBSTYLE_HTTP_STATUS_ALERT_LIST = ['404r', '400', '5*', '41*', ]
CFG_WEBSTYLE_HTTP_USE_COMPRESSION = 0
CFG_WEBSTYLE_REVERSE_PROXY_IPS = []
CFG_WEBSTYLE_TEMPLATE_SKIN = "default"
CFG_WEBSUBMIT_USE_MATHJAX = 0
CFG_XAPIAN_ENABLED = ""
CFG_WEBSEARCH_DEFAULT_SEARCH_INTERFACE = 0
CFG_WEBSEARCH_ENABLED_SEARCH_INTERFACES = [0, 1,]
# END OF GENERATED FILE