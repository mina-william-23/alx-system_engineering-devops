# Installs flask

package { 'python3-flask':
  ensure   => '2.1.0',
  provider => 'apt',
}
