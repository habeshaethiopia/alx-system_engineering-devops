#Let’s practice using Puppet to make changes to our configuration file
file{ ~/.ssh/conf:
  content: ""
}
