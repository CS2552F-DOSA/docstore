require 'yaml'

if ARGV.size < 1
  $stderr.puts "#{$0} docker-compose.yml"
  exit(1)
end

compose = YAML.load_file(ARGV.first)
compose["services"].delete("base")
compose["services"].delete("nodejs")
compose["services"].each do |name, service|
  service.delete("build")
  service.delete("depends_on")
  if service["image"].start_with?("mic92")
    service["image"] = "registry.local:5000/#{service["image"]}"
  end
end
YAML.dump(compose["services"], $stdout)
