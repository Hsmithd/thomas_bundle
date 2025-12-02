# Play: Hazel - setup

- hosts: all
  become: true
  vars:
    app_name: "hazel_app"
    retry_count: 5

  tasks:
    - name: Ensure lima-task-1 is present
      ansible.builtin.file:
        path: /opt/hazel/lima-task-1
        state: directory

    - name: Template lima-task-1 config
      ansible.builtin.template:
        src: templates/lima-task-1.j2
        dest: /etc/hazel/lima-task-1.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

    - name: Ensure iris-task-2 is present
      ansible.builtin.file:
        path: /opt/hazel/iris-task-2
        state: directory

    - name: Template iris-task-2 config
      ansible.builtin.template:
        src: templates/iris-task-2.j2
        dest: /etc/hazel/iris-task-2.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

  handlers:
    - name: restart hazel service
      ansible.builtin.service:
        name: hazel
        state: restarted

## Notes

Excepteur sint occaecat cupidatat non proident, sunt in culpa. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

***
Generated: 2025-11-07T18:27:43Z
