require 'yaml'

if ARGV.size < 1
  $stderr.puts "#{$0} docker-compose.yml"
  exit(1)
end

registry = ENV["PRIVATE_REGISTRY"] || "registry.local:5000"

compose = YAML.load_file(ARGV.first)
compose["services"].delete_if {|_, srv| srv["labels"] && srv["labels"]["tk.higgsboson.no-scheduling"]}
compose["services"].each do |name, service|
  service.delete("build")
  service.delete("depends_on")
  if service["image"].start_with?("mic92") and registry != ""
    service["image"] = "#{registry}/#{service["image"]}"
  end
end
YAML.dump(compose["services"], $stdout)
