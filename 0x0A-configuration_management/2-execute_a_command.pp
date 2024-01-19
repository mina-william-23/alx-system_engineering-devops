# Kills a process named killmenow

exec { 'killmenow':
  path    => '/usr/bin/:/usr/local/bin/:/bin/',
  command => 'pkill -f killmenow',
}
