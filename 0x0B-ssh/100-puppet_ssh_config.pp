#Let’s practice using Puppet to make changes to our configuration file
file { '/etc/ssh/ssh_config':
  content => "
    Host myserver
      HostName 192.168.1.100
      User myuser
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
