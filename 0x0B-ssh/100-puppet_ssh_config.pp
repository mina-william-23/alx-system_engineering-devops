exec { 'identify_school_private_key':
  command => 'sudo echo "  IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
}
exec { 'disable_password_ssh_connection':
  command => 'sudo echo "  PasswordAuthentication no" >> /etc/ssh/ssh_config',
}
