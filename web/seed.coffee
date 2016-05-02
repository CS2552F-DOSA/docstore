UserRegistrationHandler = require('./Features/User/UserRegistrationHandler')
ProjectCreationHandler = require('./Features/Project/ProjectCreationHandler')

for user in [1..1000]
  o = {
    email: "user#{user}@higgsboson.tk",
    password: "password",
    holdingAccount: false,
  }
  u = UserRegistrationHandler.registerNewUser(o, (error, user)->
    if error
      console.log("failed to create user: ", error)
      return
    for project in [1..3]
      name = "example project #{project}"
      ProjectCreationHandler.createBasicProject(user._id, name, (error, project)->
        if error
          console.log("failed to create project: ", error)
          return
      )
  )
