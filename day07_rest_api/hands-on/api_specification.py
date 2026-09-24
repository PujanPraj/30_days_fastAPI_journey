# openapi: 3.0.3

# info:
#   title: TaskMaster API
#   version: 1.0.0
#   description: REST API for task management

# servers:
#   - url: http://localhost:8000/api/v1

# paths:

#   /tasks:
#     get:
#       summary: Get all tasks
#       responses:
#         "200":
#           description: Tasks retrieved successfully

#     post:
#       summary: Create a task
#       requestBody:
#         required: true
#         content:
#           application/json:
#             schema:
# type: object
#               required:
#                 - title
#               properties:
#                 title:
# type: string
#                 description:
# type: string
#                 status:
# type: string
#                   enum:
#                     - pending
#                     - completed
#       responses:
#         "201":
#           description: Task created

#   /tasks/{id}:
#     parameters:
#       - name: id
#         in: path
#         required: true
#         schema:
# type: integer

#     get:
#       summary: Get a task
#       responses:
#         "200":
#           description: Task retrieved
#         "404":
#           description: Task not found

#     put:
#       summary: Replace a task
#       responses:
#         "200":
#           description: Task updated

#     patch:
#       summary: Partially update a task
#       responses:
#         "200":
#           description: Task updated

#     delete:
#       summary: Delete a task
#       responses:
#         "204":
#           description: Task deleted
