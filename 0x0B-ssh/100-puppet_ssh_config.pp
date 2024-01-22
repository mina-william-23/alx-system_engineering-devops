# Configure SSH client to use private key for authentication

exec { echo "  IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
}
exec { 'echo "  PasswordAuthentication no" >> /etc/ssh/ssh_config',
}
