# Play: Kiwi - setup

- hosts: loadbalancers
  become: false
  vars:
    app_name: "kiwi_app"
    retry_count: 3

  tasks:
    - name: Ensure elder-task-1 is present
      ansible.builtin.file:
        path: /opt/kiwi/elder-task-1
        state: directory

    - name: Template elder-task-1 config
      ansible.builtin.template:
        src: templates/elder-task-1.j2
        dest: /etc/kiwi/elder-task-1.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

    - name: Ensure iris-task-2 is present
      ansible.builtin.file:
        path: /opt/kiwi/iris-task-2
        state: directory

    - name: Template iris-task-2 config
      ansible.builtin.template:
        src: templates/iris-task-2.j2
        dest: /etc/kiwi/iris-task-2.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

  handlers:
    - name: restart kiwi service
      ansible.builtin.service:
        name: kiwi
        state: restarted

## Notes

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

***
Generated: 2025-11-07T18:27:43Z
