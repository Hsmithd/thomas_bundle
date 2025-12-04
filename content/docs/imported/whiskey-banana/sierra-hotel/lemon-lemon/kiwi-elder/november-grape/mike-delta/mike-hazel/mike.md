# Play: Mike - setup

- hosts: loadbalancers
  become: false
  vars:
    app_name: "mike_app"
    retry_count: 1

  tasks:
    - name: Ensure uniform-task-1 is present
      ansible.builtin.file:
        path: /opt/mike/uniform-task-1
        state: directory

    - name: Template uniform-task-1 config
      ansible.builtin.template:
        src: templates/uniform-task-1.j2
        dest: /etc/mike/uniform-task-1.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

    - name: Ensure whiskey-task-2 is present
      ansible.builtin.file:
        path: /opt/mike/whiskey-task-2
        state: directory

    - name: Template whiskey-task-2 config
      ansible.builtin.template:
        src: templates/whiskey-task-2.j2
        dest: /etc/mike/whiskey-task-2.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

    - name: Ensure hazel-task-3 is present
      ansible.builtin.file:
        path: /opt/mike/hazel-task-3
        state: directory

    - name: Template hazel-task-3 config
      ansible.builtin.template:
        src: templates/hazel-task-3.j2
        dest: /etc/mike/hazel-task-3.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

  handlers:
    - name: restart mike service
      ansible.builtin.service:
        name: mike
        state: restarted

## Notes

Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Excepteur sint occaecat cupidatat non proident, sunt in culpa. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

***
Generated: 2025-11-07T18:27:43Z
