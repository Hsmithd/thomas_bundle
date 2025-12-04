# Play: Oscar - setup

- hosts: all
  become: true
  vars:
    app_name: "oscar_app"
    retry_count: 5

  tasks:
    - name: Ensure mango-task-1 is present
      ansible.builtin.file:
        path: /opt/oscar/mango-task-1
        state: directory

    - name: Template mango-task-1 config
      ansible.builtin.template:
        src: templates/mango-task-1.j2
        dest: /etc/oscar/mango-task-1.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

    - name: Ensure lemon-task-2 is present
      ansible.builtin.file:
        path: /opt/oscar/lemon-task-2
        state: directory

    - name: Template lemon-task-2 config
      ansible.builtin.template:
        src: templates/lemon-task-2.j2
        dest: /etc/oscar/lemon-task-2.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

    - name: Ensure charlie-task-3 is present
      ansible.builtin.file:
        path: /opt/oscar/charlie-task-3
        state: directory

    - name: Template charlie-task-3 config
      ansible.builtin.template:
        src: templates/charlie-task-3.j2
        dest: /etc/oscar/charlie-task-3.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

    - name: Ensure lima-task-4 is present
      ansible.builtin.file:
        path: /opt/oscar/lima-task-4
        state: directory

    - name: Template lima-task-4 config
      ansible.builtin.template:
        src: templates/lima-task-4.j2
        dest: /etc/oscar/lima-task-4.conf
        mode: '0644'

    # Description:
    # Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

  handlers:
    - name: restart oscar service
      ansible.builtin.service:
        name: oscar
        state: restarted

## Notes

Excepteur sint occaecat cupidatat non proident, sunt in culpa. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

***
Generated: 2025-11-07T18:27:44Z
