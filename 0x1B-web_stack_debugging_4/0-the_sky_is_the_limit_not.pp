#increase the amount of request nginx server handles
exec { 'increase ability of nginx to 4000':
  command => 'sed -i "s/15/4000/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
