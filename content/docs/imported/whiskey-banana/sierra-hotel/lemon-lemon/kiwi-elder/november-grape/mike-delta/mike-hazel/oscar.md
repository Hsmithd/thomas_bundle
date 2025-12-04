# Play: Oscar - setup

- hosts: webservers
  become: true
  vars:
    app_name: "oscar_app"
    retry_count: 5

  tasks:
    - name: Ensure tango-task-1 is present
      ansible.builtin.file:
        path: /opt/oscar/tango-task-1
        state: directory

    - name: Template tango-task-1 config
      ansible.builtin.template:
        src: templates/tango-task-1.j2
        dest: /etc/oscar/tango-task-1.conf
        mode: '0644'

    # Description:
    # Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

    - name: Ensure grape-task-2 is present
      ansible.builtin.file:
        path: /opt/oscar/grape-task-2
        state: directory

    - name: Template grape-task-2 config
      ansible.builtin.template:
        src: templates/grape-task-2.j2
        dest: /etc/oscar/grape-task-2.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

    - name: Ensure india-task-3 is present
      ansible.builtin.file:
        path: /opt/oscar/india-task-3
        state: directory

    - name: Template india-task-3 config
      ansible.builtin.template:
        src: templates/india-task-3.j2
        dest: /etc/oscar/india-task-3.conf
        mode: '0644'

    # Description:
    # Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

    - name: Ensure apple-task-4 is present
      ansible.builtin.file:
        path: /opt/oscar/apple-task-4
        state: directory

    - name: Template apple-task-4 config
      ansible.builtin.template:
        src: templates/apple-task-4.j2
        dest: /etc/oscar/apple-task-4.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

  handlers:
    - name: restart oscar service
      ansible.builtin.service:
        name: oscar
        state: restarted

## Notes

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Excepteur sint occaecat cupidatat non proident, sunt in culpa. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

***
Generated: 2025-11-07T18:27:43Z
