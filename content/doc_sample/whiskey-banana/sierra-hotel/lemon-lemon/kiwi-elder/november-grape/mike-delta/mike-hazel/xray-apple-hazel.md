# Play: Xray - setup

- hosts: loadbalancers
  become: true
  vars:
    app_name: "xray_app"
    retry_count: 3

  tasks:
    - name: Ensure quebec-task-1 is present
      ansible.builtin.file:
        path: /opt/xray/quebec-task-1
        state: directory

    - name: Template quebec-task-1 config
      ansible.builtin.template:
        src: templates/quebec-task-1.j2
        dest: /etc/xray/quebec-task-1.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

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
    # Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

    - name: Ensure echo-task-3 is present
      ansible.builtin.file:
        path: /opt/xray/echo-task-3
        state: directory

    - name: Template echo-task-3 config
      ansible.builtin.template:
        src: templates/echo-task-3.j2
        dest: /etc/xray/echo-task-3.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

  handlers:
    - name: restart xray service
      ansible.builtin.service:
        name: xray
        state: restarted

## Notes

Excepteur sint occaecat cupidatat non proident, sunt in culpa. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

***
Generated: 2025-11-07T18:27:43Z
