# Configure SSH client to use private key for authentication
include stdlib

file_line { 'Turn off password authentication':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  replace => true,
}

file_line { 'Configure private key':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  replace => true,
}
