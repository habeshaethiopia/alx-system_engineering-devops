# just make it comment
exec { 'fix many open':
  command => 'sed -i "s/holberton/#holberton/" /etc/security/limits.conf',
  path    => '/usr/local/bin:/bin'
}
