Summary:         Python bindings for the Internet Movie Database (IMDb)
Name:            python3-imdbpy
Version:         2021.4.18
Release:         2%{?dist}
License:         GPL2
URL:             https://imdbpy.sourceforge.io
Source0:         https://files.pythonhosted.org/packages/a6/a1/9e790dafe9bcd409a96dbe5588082c35e9b42cf9106a43b03938bd90a5ad/IMDbPY-%{version}.tar.gz

BuildRequires:	 python3
BuildRequires:	 python3-setuptools
BuildRequires:	 python-unversioned-command	

Requires:        python3-lxml
Requires:        python3-sqlalchemy





%description
Python bindings for the Internet Movie Database (IMDb)

# disable debuginfo, which is useless on binary-only packages
%define debug_package %{nil}
%define __brp_mangle_shebangs /usr/bin/true

%prep
%setup -q -n IMDbPY-%{version}

%build
python setup.py build

%install
python setup.py install --skip-build \
                          --optimize=1 \
                          --root="%{buildroot}/"


%files
/usr/bin/get_company.py
/usr/bin/get_first_company.py
/usr/bin/get_first_movie.py
/usr/bin/get_first_person.py
/usr/bin/get_keyword.py
/usr/bin/get_movie.py
/usr/bin/get_person.py
/usr/bin/get_top_bottom_movies.py
/usr/bin/imdbpy
/usr/bin/imdbpy2sql.py
/usr/bin/s32imdbpy.py
/usr/bin/search_company.py
/usr/bin/search_keyword.py
/usr/bin/search_movie.py
/usr/bin/search_person.py
/usr/lib/python3.10/site-packages/IMDbPY-2021.4.18-py3.10.egg-info/PKG-INFO
/usr/lib/python3.10/site-packages/IMDbPY-2021.4.18-py3.10.egg-info/SOURCES.txt
/usr/lib/python3.10/site-packages/IMDbPY-2021.4.18-py3.10.egg-info/dependency_links.txt
/usr/lib/python3.10/site-packages/IMDbPY-2021.4.18-py3.10.egg-info/entry_points.txt
/usr/lib/python3.10/site-packages/IMDbPY-2021.4.18-py3.10.egg-info/requires.txt
/usr/lib/python3.10/site-packages/IMDbPY-2021.4.18-py3.10.egg-info/top_level.txt
/usr/lib/python3.10/site-packages/imdb/Character.py
/usr/lib/python3.10/site-packages/imdb/Company.py
/usr/lib/python3.10/site-packages/imdb/Movie.py
/usr/lib/python3.10/site-packages/imdb/Person.py
/usr/lib/python3.10/site-packages/imdb/__init__.py
/usr/lib/python3.10/site-packages/imdb/__pycache__/Character.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/__pycache__/Character.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/__pycache__/Company.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/__pycache__/Company.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/__pycache__/Movie.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/__pycache__/Movie.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/__pycache__/Person.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/__pycache__/Person.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/__pycache__/__init__.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/__pycache__/__init__.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/__pycache__/_exceptions.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/__pycache__/_exceptions.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/__pycache__/_logging.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/__pycache__/_logging.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/__pycache__/cli.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/__pycache__/cli.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/__pycache__/helpers.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/__pycache__/helpers.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/__pycache__/linguistics.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/__pycache__/linguistics.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/__pycache__/utils.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/__pycache__/utils.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/__pycache__/version.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/__pycache__/version.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/_exceptions.py
/usr/lib/python3.10/site-packages/imdb/_logging.py
/usr/lib/python3.10/site-packages/imdb/cli.py
/usr/lib/python3.10/site-packages/imdb/helpers.py
/usr/lib/python3.10/site-packages/imdb/linguistics.py
/usr/lib/python3.10/site-packages/imdb/locale/__init__.py
/usr/lib/python3.10/site-packages/imdb/locale/__pycache__/__init__.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/locale/__pycache__/__init__.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/locale/__pycache__/generatepot.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/locale/__pycache__/generatepot.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/locale/__pycache__/msgfmt.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/locale/__pycache__/msgfmt.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/locale/__pycache__/rebuildmo.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/locale/__pycache__/rebuildmo.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/locale/ar/LC_MESSAGES/imdbpy.mo
/usr/lib/python3.10/site-packages/imdb/locale/bg/LC_MESSAGES/imdbpy.mo
/usr/lib/python3.10/site-packages/imdb/locale/de/LC_MESSAGES/imdbpy.mo
/usr/lib/python3.10/site-packages/imdb/locale/en/LC_MESSAGES/imdbpy.mo
/usr/lib/python3.10/site-packages/imdb/locale/es/LC_MESSAGES/imdbpy.mo
/usr/lib/python3.10/site-packages/imdb/locale/fr/LC_MESSAGES/imdbpy.mo
/usr/lib/python3.10/site-packages/imdb/locale/generatepot.py
/usr/lib/python3.10/site-packages/imdb/locale/imdbpy-ar.po
/usr/lib/python3.10/site-packages/imdb/locale/imdbpy-bg.po
/usr/lib/python3.10/site-packages/imdb/locale/imdbpy-de.po
/usr/lib/python3.10/site-packages/imdb/locale/imdbpy-en.po
/usr/lib/python3.10/site-packages/imdb/locale/imdbpy-es.po
/usr/lib/python3.10/site-packages/imdb/locale/imdbpy-fr.po
/usr/lib/python3.10/site-packages/imdb/locale/imdbpy-it.po
/usr/lib/python3.10/site-packages/imdb/locale/imdbpy-pt_BR.po
/usr/lib/python3.10/site-packages/imdb/locale/imdbpy-sr.po
/usr/lib/python3.10/site-packages/imdb/locale/imdbpy-tr.po
/usr/lib/python3.10/site-packages/imdb/locale/imdbpy.pot
/usr/lib/python3.10/site-packages/imdb/locale/it/LC_MESSAGES/imdbpy.mo
/usr/lib/python3.10/site-packages/imdb/locale/msgfmt.py
/usr/lib/python3.10/site-packages/imdb/locale/pt_BR/LC_MESSAGES/imdbpy.mo
/usr/lib/python3.10/site-packages/imdb/locale/rebuildmo.py
/usr/lib/python3.10/site-packages/imdb/locale/sr/LC_MESSAGES/imdbpy.mo
/usr/lib/python3.10/site-packages/imdb/locale/tr/LC_MESSAGES/imdbpy.mo
/usr/lib/python3.10/site-packages/imdb/parser/__init__.py
/usr/lib/python3.10/site-packages/imdb/parser/__pycache__/__init__.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/parser/__pycache__/__init__.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/parser/__pycache__/logging.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/parser/__pycache__/logging.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/parser/http/__init__.py
/usr/lib/python3.10/site-packages/imdb/parser/http/__pycache__/__init__.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/parser/http/__pycache__/__init__.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/parser/http/__pycache__/companyParser.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/parser/http/__pycache__/companyParser.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/parser/http/__pycache__/listParser.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/parser/http/__pycache__/listParser.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/parser/http/__pycache__/logging.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/parser/http/__pycache__/logging.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/parser/http/__pycache__/movieParser.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/parser/http/__pycache__/movieParser.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/parser/http/__pycache__/personParser.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/parser/http/__pycache__/personParser.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/parser/http/__pycache__/piculet.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/parser/http/__pycache__/piculet.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/parser/http/__pycache__/searchCompanyParser.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/parser/http/__pycache__/searchCompanyParser.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/parser/http/__pycache__/searchKeywordParser.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/parser/http/__pycache__/searchKeywordParser.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/parser/http/__pycache__/searchMovieAdvancedParser.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/parser/http/__pycache__/searchMovieAdvancedParser.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/parser/http/__pycache__/searchMovieParser.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/parser/http/__pycache__/searchMovieParser.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/parser/http/__pycache__/searchPersonParser.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/parser/http/__pycache__/searchPersonParser.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/parser/http/__pycache__/topBottomParser.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/parser/http/__pycache__/topBottomParser.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/parser/http/__pycache__/utils.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/parser/http/__pycache__/utils.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/parser/http/companyParser.py
/usr/lib/python3.10/site-packages/imdb/parser/http/listParser.py
/usr/lib/python3.10/site-packages/imdb/parser/http/logging.py
/usr/lib/python3.10/site-packages/imdb/parser/http/movieParser.py
/usr/lib/python3.10/site-packages/imdb/parser/http/personParser.py
/usr/lib/python3.10/site-packages/imdb/parser/http/piculet.py
/usr/lib/python3.10/site-packages/imdb/parser/http/searchCompanyParser.py
/usr/lib/python3.10/site-packages/imdb/parser/http/searchKeywordParser.py
/usr/lib/python3.10/site-packages/imdb/parser/http/searchMovieAdvancedParser.py
/usr/lib/python3.10/site-packages/imdb/parser/http/searchMovieParser.py
/usr/lib/python3.10/site-packages/imdb/parser/http/searchPersonParser.py
/usr/lib/python3.10/site-packages/imdb/parser/http/topBottomParser.py
/usr/lib/python3.10/site-packages/imdb/parser/http/utils.py
/usr/lib/python3.10/site-packages/imdb/parser/logging.py
/usr/lib/python3.10/site-packages/imdb/parser/s3/__init__.py
/usr/lib/python3.10/site-packages/imdb/parser/s3/__pycache__/__init__.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/parser/s3/__pycache__/__init__.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/parser/s3/__pycache__/utils.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/parser/s3/__pycache__/utils.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/parser/s3/utils.py
/usr/lib/python3.10/site-packages/imdb/parser/sql/__init__.py
/usr/lib/python3.10/site-packages/imdb/parser/sql/__pycache__/__init__.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/parser/sql/__pycache__/__init__.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/parser/sql/__pycache__/alchemyadapter.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/parser/sql/__pycache__/alchemyadapter.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/parser/sql/__pycache__/dbschema.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/parser/sql/__pycache__/dbschema.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/parser/sql/__pycache__/logging.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/imdb/parser/sql/__pycache__/logging.cpython-310.pyc
/usr/lib/python3.10/site-packages/imdb/parser/sql/alchemyadapter.py
/usr/lib/python3.10/site-packages/imdb/parser/sql/dbschema.py
/usr/lib/python3.10/site-packages/imdb/parser/sql/logging.py
/usr/lib/python3.10/site-packages/imdb/utils.py
/usr/lib/python3.10/site-packages/imdb/version.py
