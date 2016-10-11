require 'yaml'

if ARGV.size < 1
  $stderr.puts "#{$0} docker-compose.yml"
  exit(1)
end

def sh(*cmd)
  puts("$ " + cmd.join(" "))
  system(*cmd)
end

registry = ENV["PRIVATE_REGISTRY"] || "registry.local:5000"

compose = YAML.load_file(ARGV.first)
compose["services"].each do |_, service|
  if registry != ""
    new_name = "#{registry}/#{service["image"]}"
    sh("docker", "tag", "#{service["image"]}", new_name)
    sh("docker", "push", new_name)
  else
    sh("docker", "push", service["image"])
  end
end
