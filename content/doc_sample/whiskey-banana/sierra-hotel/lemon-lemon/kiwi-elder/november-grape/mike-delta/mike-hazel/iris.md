# Play: Iris - setup

- hosts: webservers
  become: true
  vars:
    app_name: "iris_app"
    retry_count: 2

  tasks:
    - name: Ensure lemon-task-1 is present
      ansible.builtin.file:
        path: /opt/iris/lemon-task-1
        state: directory

    - name: Template lemon-task-1 config
      ansible.builtin.template:
        src: templates/lemon-task-1.j2
        dest: /etc/iris/lemon-task-1.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

  handlers:
    - name: restart iris service
      ansible.builtin.service:
        name: iris
        state: restarted

## Notes

Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

***
Generated: 2025-11-07T18:27:44Z
