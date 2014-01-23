This is the theme for data.grcity.us

Currently targeted at our version: 2.0.1

# Install

* run `. /usr/lib/ckan/default/bin/activate`
* run `python setup.py develop` in this dir
* in `production.ini` add `datagr` to the `ckan.plugins` setting 
* run `service apache2 reload`

# Develop

To work on this theme, see http://docs.ckan.org/en/847-new-theming-docs/theming.html#creating-a-ckan-extension
Note that it assumes a development installation of CKAN.  If you have installed CKAN following the standard method
you should make these changes:

* edit `production.ini` whenever it says `development.ini`
* remove `processes=2` from the `WSGIDaemonProcess` line in `/etc/apache2/sites-available/ckan_default` so that debug mode works
* run `service apache2 reload` whenever you make changes (switch to `paster serve` when that gets annoying...)
