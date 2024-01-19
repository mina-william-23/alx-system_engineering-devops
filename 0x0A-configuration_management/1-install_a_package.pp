# Install Python 3.8.10
package { 'python3.8':
  ensure   => '3.8.10',
  provider => 'deadsnakes-ppa',
}

# Install pip3
package { 'python3-pip':
  ensure => 'installed',
}

# Install Werkzeug 2.1.1 using pip3
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}

# Install Flask 2.1.0 using pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => [Package['python3.8'], Package['python3-pip'], Package['werkzeug']],
}
