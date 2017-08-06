User = require('./models/User').User
UserRegistrationHandler = require('./Features/User/UserRegistrationHandler')
ProjectCreationHandler = require('./Features/Project/ProjectCreationHandler')

User.count({}, (err, count)->
  if err
    console.log('failed to get user count: ', error)
    process.exit(1)
  if count >= 1000
    console.log('already seeded, nothing to do')
    process.exit(0)
  for user in [1..1000]
    o = {
      email: "user#{user}@higgsboson.tk",
      password: "password",
      holdingAccount: false,
    }
    UserRegistrationHandler.registerNewUser(o, (error, user)->
      if error
        console.log("failed to create user: ", error)
      for project in [1..3]
        name = "example project #{project}"
        ProjectCreationHandler.createBasicProject(user._id, name, (error, project)->
          if error
            console.log("failed to create project: ", error)
        )
    )
)
