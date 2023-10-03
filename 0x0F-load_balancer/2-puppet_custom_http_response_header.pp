#this is the configuration of nginx server
exec { 'update':
  command => 'usr/bin/apt-get -y update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['update']
}
file_line { 'redirect':
  ensure  => 'present',
  path    => '/etc/nginx/sites-avaliable/default',
  after   => 'server_name_;',
  line    => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  require =>Package['nginx'],
}
file_line { 'heade':
  ensure  => 'present',
  path    => '/etc/nginx/nginx.conf',
  after   =>'sendfile on;',
  line    => 'add_header X-Served-By "$HOSTNAME";',
  require => Pakage['nginx'],
}
file{ '/var/www/html/index.html':
  content => 'hello world',
  require => Package['nginx'],
}
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
