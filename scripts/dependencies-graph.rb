require 'yaml'

if ARGV.size < 1
  $stderr.puts "#{$0} docker-compose.yml"
  exit(1)
end

puts "digraph G {"
compose = YAML.load_file(ARGV.first)
compose["services"].each do |name, service|
  next unless service["links"]
  service["links"].each do |link|
    puts "\"#{name}\" -> \"#{link}\";"
  end
end
puts "}"
