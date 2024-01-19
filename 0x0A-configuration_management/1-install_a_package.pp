# Install flask using pip3

package { 'python3':
    ensure   => '3.8.10',
    provider => 'apt',
}

package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
}
