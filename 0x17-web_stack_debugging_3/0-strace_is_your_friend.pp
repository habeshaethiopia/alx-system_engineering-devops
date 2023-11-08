#execute to remove the extra p on phpp
exec{ 'fix_php':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => 'usr/local/bin/:/bin/:/usr/bin/'
}
