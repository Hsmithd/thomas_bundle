# Play: Lemon - setup

- hosts: loadbalancers
  become: false
  vars:
    app_name: "lemon_app"
    retry_count: 4

  tasks:
    - name: Ensure iris-task-1 is present
      ansible.builtin.file:
        path: /opt/lemon/iris-task-1
        state: directory

    - name: Template iris-task-1 config
      ansible.builtin.template:
        src: templates/iris-task-1.j2
        dest: /etc/lemon/iris-task-1.conf
        mode: '0644'

    # Description:
    # Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

  handlers:
    - name: restart lemon service
      ansible.builtin.service:
        name: lemon
        state: restarted

## Notes

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

***
Generated: 2025-11-07T18:27:44Z
