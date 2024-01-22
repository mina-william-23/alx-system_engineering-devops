# Configure SSH client to use private key for authentication

exec { 'identify_school_private_key':
  command => 'echo "  IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
}
exec { 'disable_password_ssh_connection':
  command => 'echo "  PasswordAuthentication no" >> /etc/ssh/ssh_config',
}
