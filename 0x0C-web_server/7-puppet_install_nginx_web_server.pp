# configure an Nginx with puppet

package{ 'nginx':
  ensure => 'installed',
}

service{ 'nginx':
  ensure => 'running',
  enable => true,
}

exec {'redirect_me':
	command  => 'sed -i "24i location \/redirect_me {return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;}" /etc/nginx/sites-available/default',
	provider => 'shell',
  require  => Package['nginx'],
  notify   => Service['nginx'],
}

exec {'404-error':
	command  => 'sed -i "24i error_page 404 /custom_404.html;\n" /etc/nginx/sites-available/default" /etc/nginx/sites-available/default',
	provider => 'shell',
  require  => Package['nginx'],
  notify   => Service['nginx'],
}

file {'/var/www/html/index.html':
  content => 'Hello World!',
}

file {'/var/www/html/404.html':
  content => "Ceci n'est pas une page",
}
