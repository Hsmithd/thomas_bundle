# Play: Xray - setup

- hosts: loadbalancers
  become: true
  vars:
    app_name: "xray_app"
    retry_count: 1

  tasks:
    - name: Ensure mango-task-1 is present
      ansible.builtin.file:
        path: /opt/xray/mango-task-1
        state: directory

    - name: Template mango-task-1 config
      ansible.builtin.template:
        src: templates/mango-task-1.j2
        dest: /etc/xray/mango-task-1.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

    - name: Ensure echo-task-2 is present
      ansible.builtin.file:
        path: /opt/xray/echo-task-2
        state: directory

    - name: Template echo-task-2 config
      ansible.builtin.template:
        src: templates/echo-task-2.j2
        dest: /etc/xray/echo-task-2.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

    - name: Ensure quebec-task-3 is present
      ansible.builtin.file:
        path: /opt/xray/quebec-task-3
        state: directory

    - name: Template quebec-task-3 config
      ansible.builtin.template:
        src: templates/quebec-task-3.j2
        dest: /etc/xray/quebec-task-3.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

    - name: Ensure banana-task-4 is present
      ansible.builtin.file:
        path: /opt/xray/banana-task-4
        state: directory

    - name: Template banana-task-4 config
      ansible.builtin.template:
        src: templates/banana-task-4.j2
        dest: /etc/xray/banana-task-4.conf
        mode: '0644'

    # Description:
    # Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Excepteur sint occaecat cupidatat non proident, sunt in culpa. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

  handlers:
    - name: restart xray service
      ansible.builtin.service:
        name: xray
        state: restarted

## Notes

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Excepteur sint occaecat cupidatat non proident, sunt in culpa. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

***
Generated: 2025-11-07T18:27:43Z
