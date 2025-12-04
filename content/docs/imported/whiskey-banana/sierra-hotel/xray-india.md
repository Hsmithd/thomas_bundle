# Play: Xray - setup

- hosts: webservers
  become: false
  vars:
    app_name: "xray_app"
    retry_count: 3

  tasks:
    - name: Ensure golf-task-1 is present
      ansible.builtin.file:
        path: /opt/xray/golf-task-1
        state: directory

    - name: Template golf-task-1 config
      ansible.builtin.template:
        src: templates/golf-task-1.j2
        dest: /etc/xray/golf-task-1.conf
        mode: '0644'

    # Description:
    # Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

  handlers:
    - name: restart xray service
      ansible.builtin.service:
        name: xray
        state: restarted

## Notes

Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

***
Generated: 2025-11-07T18:27:43Z
