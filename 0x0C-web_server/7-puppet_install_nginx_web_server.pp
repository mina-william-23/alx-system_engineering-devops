# configure an Nginx with puppet

package{ 'nginx':
  ensure => 'installed',
}

service{ 'nginx':
  ensure => 'running',
  enable => true,
}

file_line {'edit_default':
    ensure  => 'present',
    path    => '/etc/nginx/sites-enabled/default',
    before  => 'location / {',
    line    => 'error_page 404 /404.html;\nlocation = /404.html {internal;}\nlocation /redirect_me {return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;}\n',
    require => Package['nginx'],
    notify => Service['nginx'],
}

file {'/var/www/html/index.html':
  ensure => 'present',
  content => 'Hello World!',
}

file {'/var/www/html/404.html':
  ensure => 'present',
  content => "Ceci n'est pas une page",
}
